import os
import json
from unittest import mock, TestCase

import pytest
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.response import Response
from django.core.files import File

from api.models import Image, PDF
from api.views import RotateImageView, ConvertPDFView

from dotenv import load_dotenv

load_dotenv()


class TestAPI(TestCase):
    def setUp(self):
        self.client = APIClient()

        mocker = mock.MagicMock(file=File)
        mocker.img = "images/sample.png"
        mocker.pdf = "pdfs/sample.pdf"

        self.image = Image.objects.create(
            image_path=mocker.img, width=100, height=100, channels=3
        )
        self.pdf = PDF.objects.create(
            pdf_path=mocker.pdf, width=100, height=100, num_pages=3
        )

    def _get_response_content_as_json(self, response):
        return json.loads(response.content.decode("utf-8"))

    @pytest.mark.django_db
    def test_upload_image_base64(self):
        response = self.client.post(
            "/api/upload", {"upload": os.environ.get("IMAGE_BASE64")}, format="json"
        )
        assert Image.objects.count() == 2
        assert response.status_code == status.HTTP_201_CREATED
        assert b"image" in response.content

    @pytest.mark.django_db
    def test_upload_pdf_base64(self):
        response = self.client.post(
            "/api/upload", {"upload": os.environ.get("PDF_BASE64")}, format="json"
        )
        assert PDF.objects.count() == 2
        assert response.status_code == status.HTTP_201_CREATED
        assert b"pdf" in response.content

    @pytest.mark.django_db
    def test_list_image(self):
        response = self.client.get("/api/images")
        assert Image.objects.count() == 1
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_list_pdf(self):
        response = self.client.get("/api/pdfs")
        assert PDF.objects.count() == 1
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_retrieve_image(self):
        response = self.client.get(f"/api/images/{self.image.id}")
        data = self._get_response_content_as_json(response)

        assert Image.objects.count() == 1
        assert response.status_code == status.HTTP_200_OK
        assert data["id"] == self.image.id
        assert data["image_path"] == "http://testserver/media/images/sample.png"
        assert data["width"] == 100
        assert data["height"] == 100
        assert data["channels"] == 3

    @pytest.mark.django_db
    def test_retrieve_pdf(self):
        response = self.client.get(f"/api/pdfs/{self.pdf.id}")
        data = self._get_response_content_as_json(response)

        assert PDF.objects.count() == 1
        assert response.status_code == status.HTTP_200_OK
        assert data["id"] == self.pdf.id
        assert data["pdf_path"] == "http://testserver/media/pdfs/sample.pdf"
        assert data["width"] == "100.00"
        assert data["height"] == "100.00"
        assert data["num_pages"] == 3

    @pytest.mark.django_db
    def test_delete_image(self):
        response = self.client.delete(f"/api/images/{self.image.id}")
        assert Image.objects.count() == 0
        assert response.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.django_db
    def test_delete_pdf(self):
        response = self.client.delete(f"/api/pdfs/{self.pdf.id}")
        assert PDF.objects.count() == 0
        assert response.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.django_db
    def test_rotate_image(self):
        with mock.patch.object(
            RotateImageView,
            "post",
            return_value=Response(
                {"detail": "Image updated.", "image_id": self.image.id},
                status=status.HTTP_202_ACCEPTED,
            ),
        ) as mock_rotate_image:
            response = self.client.post(
                "/api/rotate", {"image_id": self.image.id, "angle": 45}, format="json"
            )
            mock_rotate_image.assert_called_once()
        assert response.status_code == status.HTTP_202_ACCEPTED

    @pytest.mark.django_db
    def test_convert_pdf_to_image(self):
        with mock.patch.object(
            ConvertPDFView,
            "post",
            return_value=Response(
                {"detail": "Converted successfully."}, status=status.HTTP_200_OK
            ),
        ) as mock_convert_pdf:
            response = self.client.post(
                "/api/convert-pdf-to-image", {"pdf_id": self.pdf.id}, format="json"
            )
            mock_convert_pdf.assert_called_once()
        assert response.status_code == status.HTTP_200_OK
