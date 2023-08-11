""" api app serializers. """

from rest_framework import serializers
import re
from .models import Image, PDF 

class UploadSerializer(serializers.Serializer):
    upload = serializers.CharField()

    def validate_upload(self, value):
        try:
            file_format, filestr = value.split(';base64,')
        except:
          raise serializers.ValidationError("this is not a base64 type")
          
        is_base64 = re.search("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$", filestr)
        if not is_base64:
            raise serializers.ValidationError("this is not a base64 type")
        return value


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'




class PDFSerializer(serializers.ModelSerializer):

    class Meta:
        model = PDF
        fields = '__all__'