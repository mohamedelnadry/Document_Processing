from .models import Image, PDF
from PIL import ImageShow


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
    @staticmethod
    def imageId(image_id):
        image = Image.objects.get(id=image_id)
        if not image:
            return None

        return image
    def update_image(rotated_image, image_id):
        image = ApiServices.imageId(image_id)
        return image.objects.update(image_path=rotated_image)