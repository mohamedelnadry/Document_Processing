""" API views app. """

# Django imports
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .models import Image, PDF
from .serializers import UploadSerializer, ImageSerializer, PDFSerializer
from .services import ApiServices


class UploadView(APIView):
    """Handles uploading of documents."""

    def post(self, request):
        serializer = UploadSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"detail": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        document = serializer.validated_data["upload"]
        upload_image_or_pdf, file_type = ApiServices.upload_image_or_pdf(document)
        if upload_image_or_pdf:
            return Response(
                {
                    "detail": "File uploaded successfully.",
                    "id": upload_image_or_pdf.id,
                    "file_type": file_type,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "detail": "Unable to upload. Please upload files with extensions: [pdf, png, jpg, jpeg, gif]."
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class ImagesListView(generics.ListAPIView):
    """Lists all images."""

    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PDFsListView(generics.ListAPIView):
    """Lists all PDFs."""

    queryset = PDF.objects.all()
    serializer_class = PDFSerializer


class ImageDeleteRetrieveView(generics.RetrieveDestroyAPIView):
    """Retrieve or delete an image."""

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response(
            {"detail": "Image deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


class PDFDeleteRetrieveView(generics.RetrieveDestroyAPIView):
    """Retrieve or delete a PDF."""

    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response(
            {"detail": "PDF deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )


class RotateImageView(APIView):
    """Rotates an image."""

    def post(self, request):
        image_id = request.data["image_id"]
        angle = request.data["angle"]

        updated_image = ApiServices.update_image_rotation(angle, image_id)
        if updated_image:
            return Response(
                {"detail": "Image updated.", "image_id": updated_image.id},
                status=status.HTTP_202_ACCEPTED,
            )

        return Response(
            {"detail": "Unable to rotate image."},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ConvertPDFView(APIView):
    """Converts a PDF to an image."""

    def post(self, request):
        pdf_id = request.data["pdf_id"]
        converted_data = ApiServices.convert_pdf_to_images(pdf_id)

        if converted_data:
            return Response(
                {"detail": "Converted successfully.", "data": converted_data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"detail": "Unable to convert PDF to image."},
            status=status.HTTP_400_BAD_REQUEST,
        )
