from django.db import models

# Create your models here.

class Image(models.Model):
    image_path = models.FileField(upload_to='images')
    width = models.IntegerField()
    height = models.IntegerField()
    channels = models.PositiveIntegerField()



    class Meta:
        verbose_name = ("Image")
        verbose_name_plural = ("Images")

    def __str__(self):
        return str(self.id)



class PDF(models.Model):
    pdf_path = models.FileField(upload_to='pdfs')
    width = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    num_pages = models.PositiveIntegerField()


    class Meta:
        verbose_name = ("PDF")
        verbose_name_plural = ("PDFs")

    def __str__(self):
        return str(self.id)
