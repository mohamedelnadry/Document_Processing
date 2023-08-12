""" api app admin. """
from django.contrib import admin
from .models import Image, PDF

class ImageAdmin(admin.ModelAdmin):
    """Admin display settings for Image model."""
    list_display = ['id', 'image_path', 'width', 'height', 'channels']
    search_fields = ['id', 'image_path']
    list_filter = ['channels']

admin.site.register(Image, ImageAdmin)

class PDFAdmin(admin.ModelAdmin):
    """Admin display settings for Pdf model."""
    list_display = ['id', 'pdf_path', 'width', 'height', 'num_pages']
    search_fields = ['id', 'pdf_path']
    list_filter = ['num_pages']

admin.site.register(PDF, PDFAdmin)
