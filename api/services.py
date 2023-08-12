from .models import Image, PDF
from django.core.files.base import ContentFile
from pdf2image import convert_from_path
from .utils import get_image_data


class ApiServices:
    @staticmethod
    def createImage(file_data, width, height, channels):
        create_image = Image.objects.create(
            image_path=file_data, width=width, height=height, channels=channels
        )
        if not create_image:
            return None

        return create_image

    @staticmethod
    def createPDF(file_data, width, height, num_pages):
        create_pdf = PDF.objects.create(
            pdf_path=file_data, width=width, height=height, num_pages=num_pages
        )
        if not create_pdf:
            return None

        return create_pdf

    def get_image_byID(image_id):
        try:
            image = Image.objects.get(id=image_id)
            return image

        except:
            return None

    @staticmethod
    def update_image(angle, image_id):
        from PIL import Image

        image = ApiServices.get_image_byID(image_id)

        if image:
            image_path = image.image_path.path  # Get the server's filesystem path

            img = Image.open(image_path)
            rotated_img = img.rotate(int(angle))

            # Save the rotated image directly to the file path, overwriting the original
            rotated_img.save(image_path, format=img.format)

            # Refresh the FileField to reflect changes
            image.image_path = image.image_path

            image.save()

            return image
        return None

    def convert_to_image(pdf_id):
        pdf = PDF.objects.get(id=pdf_id)
        pdf_path = pdf.pdf_path.path
        pdf_name = pdf.pdf_path.name.split("/")[1].split(".")[0]
        created_image_data = []
        if pdf:
            images = convert_from_path(pdf_path)
            for i in range(len(images)):
                width, height = images[i].size
                channels = len(images[i].getbands())
                image_path = "images/" + pdf_name + f"({i})" + ".jpg"
                images[i].save("media/" + image_path)
                created_image = Image.objects.create(
                    image_path=image_path, width=width, height=height, channels=channels
                )
                image_data = {
                    "id": created_image.id,
                    "image_path": created_image.image_path.url,
                    "width": created_image.width,
                    "height": created_image.height,
                    "channels": created_image.channels,
                }

                created_image_data.append(image_data)
            return created_image_data
        return None
