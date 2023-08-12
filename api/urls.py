"""
URL configuration for the api app.
"""

from django.urls import path
from .views import (
    UploadView,
    ImagesListView,
    PDFsListView,
    ImageDeleteRetrieveView,
    PDFDeleteRetrieveView,
    RotateImageView,
    ConvertPDFView,
)

urlpatterns = [
    # Upload routes
    path("upload", UploadView.as_view(), name="upload_image_pdf"),
    # List routes
    path("images", ImagesListView.as_view(), name="list_images"),
    path("pdfs", PDFsListView.as_view(), name="list_pdfs"),
    # Image operation routes
    path("images/<pk>", ImageDeleteRetrieveView.as_view(), name="manage_image"),
    path("rotate", RotateImageView.as_view(), name="rotate_image"),
    # PDF operation routes
    path("pdfs/<pk>", PDFDeleteRetrieveView.as_view(), name="manage_pdf"),
    path("convert-pdf-to-image", ConvertPDFView.as_view(), name="convert_pdf_to_image"),
]
