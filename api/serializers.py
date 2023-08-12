"""Serializers for the api app."""

import re
from rest_framework import serializers
from .models import Image, PDF


class UploadSerializer(serializers.Serializer):
    """
    Serializer for uploading files in base64 format.
    """
    upload = serializers.CharField()

    def validate_upload(self, value):
        """
        Validates that the provided value is in base64 format.
        """
        try:
            file_format, filestr = value.split(';base64,')
        except ValueError:
            raise serializers.ValidationError("Invalid base64 format.")
          
        is_base64 = re.search("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$", filestr)
        if not is_base64:
            raise serializers.ValidationError("Invalid base64 format.")
        return value


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for the Image model."""

    class Meta:
        model = Image
        fields = '__all__'


class PDFSerializer(serializers.ModelSerializer):
    """Serializer for the PDF model."""

    class Meta:
        model = PDF
        fields = '__all__'
