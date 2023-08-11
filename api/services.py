from .models import Image, PDF
from PIL import ImageShow


class ApiServices:
    @staticmethod
    def CreateImage(file_data, width, height, channels):
        create_image = Image.objects.create(
            image_path=file_data, width=width, height=height, channels=channels
        )
        if not create_image:
            return None

        return create_image

    @staticmethod
    def CreatePDF(file_data, width, height, num_pages):
        create_pdf = PDF.objects.create(
            pdf_path=file_data, width=width, height=height, num_pages=num_pages
        )
        if not create_pdf:
            return None

        return create_pdf
