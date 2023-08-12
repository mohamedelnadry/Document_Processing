""" api app veiws. """
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UploadSerializer, ImageSerializer, PDFSerializer
from .services import ApiServices
from .utils import base64_convert, get_pdf_data, get_image_data
from .models import Image, PDF
import json


class UploadVeiws(APIView):
    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"detail": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        document = serializer.validated_data["upload"]
        file_data, ext = base64_convert(data=document)

        if ext == "pdf":
            width, height, num_pages = get_pdf_data(file_data)
            pdf = ApiServices.createPDF(file_data, width, height, num_pages)
            if pdf:
                return Response(
                    {"detail": "file uploaded successfuly", "id": pdf.id},
                    status=status.HTTP_201_CREATED,
                )

        if ext in ["png", "jpg", "jpeg", "gif"]:
            width, height, channels = get_image_data(file_data)
            image = ApiServices.createImage(file_data, width, height, channels)
            if image:
                return Response(
                    {"detail": "file uploaded successfuly", "id": image.id},
                    status=status.HTTP_201_CREATED,
                )

        return Response(
            {
                "detail": "The provided file type is not supported. Please upload a valid image or PDF."
            },
            status=status.HTTP_201_CREATED,
        )


class Images(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PDFs(generics.ListAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer


class DeleteVeiwImage(generics.RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class DeleteRetriveImage(generics.RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def delete(self, request, *args, **kwargs):
        delete = self.destroy(request, *args, **kwargs)

        return Response(
            {"detail": "image Deleted successfuly"},
            status=status.HTTP_204_NO_CONTENT,
        )


class DeleteRetrivePDF(generics.RetrieveDestroyAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

    def delete(self, request, *args, **kwargs):
        delete = self.destroy(request, *args, **kwargs)
        return Response(
            {"detail": "file Deleted successfuly"},
            status=status.HTTP_204_NO_CONTENT,
        )


class RotateImage(APIView):
    def post(self, request):
        image_id = request.data["image_id"]
        angle = request.data["angle"]

        update_image = ApiServices.update_image(angle, image_id)
        if update_image:
            return Response(
                {"detail": "updated", "image_id": update_image.id},
                status=status.HTTP_202_ACCEPTED,
            )
        return Response(
            {"detail": "can't rotate image"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ConvertPDF(APIView):
    def post(self, request):
        pdf_id = request.data["pdf_id"]
        pdf_to_image = ApiServices.convert_to_image(pdf_id)

        if pdf_to_image:
            return Response(
                {"detail": "converted sucessfully", "data": pdf_to_image},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"detail": "can't convert pdf to image"},
            status=status.HTTP_400_BAD_REQUEST,
        )
