
""" api app admin. """
from django.contrib import admin
from .models import Image, PDF
# Register your models here.

admin.site.register(Image)
admin.site.register(PDF)
