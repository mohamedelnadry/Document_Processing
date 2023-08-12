"""
URL configuration api.
"""
from django.urls import path
from .views import UploadVeiws, Images, PDFs, DeleteRetriveImage, DeleteRetrivePDF, RotateImage, ConvertPDF

urlpatterns = [
    path('upload',UploadVeiws.as_view(),name = "upload_image_pdf"),
    path('images',Images.as_view(),name = "all_images"),
    path('pdfs',PDFs.as_view(),name = "all_pdfs"),
    path('images/<pk>',DeleteRetriveImage.as_view(),name = "delete_veiw_images"),
    path('pdfs/<pk>',DeleteRetrivePDF.as_view(),name = "delete_veiw_pdfs"),
    path('rotate',RotateImage.as_view(),name = "rotate_image"),
    path('convert-pdf-to-image',ConvertPDF.as_view(),name = "convert_pdf"),


]
