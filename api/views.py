""" api app veiws. """
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UploadSerializer
# from .services import ApiServices
from .utils import convert_base64
from PIL import Image
import PyPDF2
from io import BytesIO


class UploadVeiws(APIView):
    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"detail": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        document = serializer.validated_data['upload']
        file_data, ext = convert_base64(data = document)
        

        if ext == 'pdf':
            width, height, num_pages = get_pdf_data(file_data)

        if ext in ['png', 'jpg', 'jpeg', 'gif']:
            width, height, channels = get_image_data(file_data)
            

        

        return Response(
                {"detail": "file uploaded successfuly"},
                status=status.HTTP_201_CREATED,
            )


