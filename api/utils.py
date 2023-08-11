import base64
from django.core.files.base import ContentFile
from PIL import Image
import PyPDF2
from io import BytesIO
import random


def base64_convert(data):
    """
    Convert the given base64 data to a ContentFile and extract the file extension.

    :param data: The base64 encoded data.
    :return: A tuple containing the ContentFile and file extension
    """
    metadata, base64_encoded_data = data.split(";base64,")
    file_extension = metadata.split("/")[-1]
    number = random.randint(1,10000)

    file_content = ContentFile(
        base64.b64decode(base64_encoded_data), name=f"temp{number}.{file_extension}"
    )
    return file_content, file_extension


def get_pdf_data(file_data):
    pdf_reader = PyPDF2.PdfReader(BytesIO(file_data.read()))
    num_pages = len(pdf_reader.pages)
    page = pdf_reader.pages[0]
    width = page.mediabox.width
    height = page.mediabox.height
    return width, height, num_pages


def get_image_data(file_data):
    img = Image.open(file_data)
    width = img.size[0]
    height = img.size[1]
    channels = len(img.getbands())
    return width, height, channels

from PIL import Image

def rotate_image(image_path, angle):

    try:
        with Image.open(image_path) as img:
            rotated_img = img.rotate(int(angle))
            img.close()
            rotated_img.save(image_path)

        return image_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
