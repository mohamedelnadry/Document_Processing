"""
URL configuration api.
"""
from django.urls import path
from .views import UploadVeiws

urlpatterns = [
    path('upload',UploadVeiws.as_view(),name = "upload_image_pdf"),
]
