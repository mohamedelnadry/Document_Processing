""" model Test API App."""

import pytest
from api.models import Image, PDF
from django.urls import reverse
from unittest import mock
from django.core.files import File



class TestModel:

    @pytest.mark.django_db
    def test_image_create(self):
        mocker_image = mock.MagicMock(file=File)
        mocker_image.img="sample.png"
        image = Image.objects.create(image_path=mocker_image.img, width=100, height=100, channels=3)
        assert Image.objects.count() == 1 


    @pytest.mark.django_db
    def test_pdf_create(self):
        mocker_pdf = mock.MagicMock(file=File)
        mocker_pdf.pdf="sample.pdf"
        pdf = PDF.objects.create(pdf_path=mocker_pdf.pdf, width=100, height=100, num_pages=3)
        assert PDF.objects.count() == 1 

