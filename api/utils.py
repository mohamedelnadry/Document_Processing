""" API Utils app."""
import base64
import random
from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image
import PyPDF2


def decode_base64_to_file(data):
    """
    Convert the given base64 data to a ContentFile and extract the file extension.

    :param data: The base64 encoded data.
    :return: A tuple containing the ContentFile and file extension.
    """
    metadata, base64_encoded_data = data.split(";base64,")
    file_extension = metadata.split("/")[-1].split(";")[0]
    random_number = random.randint(1, 10000)

    decoded_data = base64.b64decode(base64_encoded_data)
    file_name = f"temp-{random_number}.{file_extension}"
    file_content = ContentFile(decoded_data, name=file_name)

    return file_content, file_extension


def extract_pdf_metadata(file_data):
    """
    Extract metadata from the given PDF file.

    :param file_data: The PDF file.
    :return: A tuple containing the width, height, and number of pages.
    """
    pdf_reader = PyPDF2.PdfReader(BytesIO(file_data.read()))
    first_page = pdf_reader.pages[0]

    width = first_page.mediabox.width
    height = first_page.mediabox.height
    num_pages = len(pdf_reader.pages)

    return width, height, num_pages


def extract_image_metadata(file_data):
    """
    Extract metadata from the given image file.

    :param file_data: The image file.
    :return: A tuple containing the width, height, and number of channels.
    """
    img = Image.open(file_data)
    width, height = img.size
    channels = len(img.getbands())

    return width, height, channels
