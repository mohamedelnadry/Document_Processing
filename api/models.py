from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images')


    class Meta:
        verbose_name = ("Image")
        verbose_name_plural = ("Images")

    def __str__(self):
        return str(self.id)



class PDF(models.Model):
    pdf = models.FileField(upload_to='pdfs')


    class Meta:
        verbose_name = ("PDF")
        verbose_name_plural = ("PDFs")

    def __str__(self):
        return str(self.id)
