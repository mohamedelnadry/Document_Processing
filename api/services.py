""" API services app."""
from django.core.files.base import ContentFile
from pdf2image import convert_from_path
from .models import Image, PDF
from .utils import decode_base64_to_file, extract_pdf_metadata, extract_image_metadata


class ApiServices:
    @staticmethod
    def upload_image_or_pdf(document):
        """
        Uploads an image or PDF after converting it from base64.
        """
        try:
            file_data, ext = decode_base64_to_file(data=document)

            if ext == "pdf":
                create_pdf = ApiServices._create_pdf(file_data)
                return create_pdf, 'pdf'

            if ext in ["png", "jpg", "jpeg", "gif"]:
                create_image = ApiServices._create_image(file_data)
                return create_image, 'image'

        except Exception as e:
            print(f"Error while uploading image or PDF: {e}")
            return None

    @staticmethod
    def _create_image(file_data):
        """
        Creates an image entry in the database.
        """
        width, height, channels = extract_image_metadata(file_data)
        return Image.objects.create(
            image_path=file_data, width=width, height=height, channels=channels
        )

    @staticmethod
    def _create_pdf(file_data):
        """
        Creates a PDF entry in the database.
        """
        width, height, num_pages = extract_pdf_metadata(file_data)
        return PDF.objects.create(
            pdf_path=file_data, width=width, height=height, num_pages=num_pages
        )

    @staticmethod
    def get_image_by_id(image_id):
        """
        Retrieve an image by its ID.
        """
        try:
            return Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            return None

    @staticmethod
    def update_image_rotation(angle, image_id):
        """
        Rotates an image by the given angle.
        """
        from PIL import Image as PilImage

        image_instance = ApiServices.get_image_by_id(image_id)

        if not image_instance:
            return None

        image_path = image_instance.image_path.path #Return Full Path to Overwrite Instance Image
        img = PilImage.open(image_path)
        rotated_img = img.rotate(int(angle))
        rotated_img.save(image_path, format=img.format)

        # Refresh the FileField to reflect changes
        image_instance.image_path = image_instance.image_path
        image_instance.save()

        return image_instance

    @staticmethod
    def convert_pdf_to_images(pdf_id):
        """
        Converts a PDF into multiple images.
        """
        try:
            pdf_instance = PDF.objects.get(id=pdf_id)
            pdf_path = pdf_instance.pdf_path.path
            pdf_name = pdf_instance.pdf_path.name.split("/")[1].split(".")[0]
            images_from_pdf = convert_from_path(pdf_path)

            created_image_data = []
            for index, image in enumerate(images_from_pdf):
                width, height = image.size
                channels = len(image.getbands())
                image_path = f"images/{pdf_name}({index}).jpg"
                image.save(f"media/{image_path}")

                new_image_instance = Image.objects.create(
                    image_path=image_path, width=width, height=height, channels=channels
                )

                image_metadata = {
                    "id": new_image_instance.id,
                    "image_path": new_image_instance.image_path.url,
                    "width": new_image_instance.width,
                    "height": new_image_instance.height,
                    "channels": new_image_instance.channels,
                }
                created_image_data.append(image_metadata)

            return created_image_data

        except Exception as e:
            print(f"Error converting PDF to images: {e}")
            return None
