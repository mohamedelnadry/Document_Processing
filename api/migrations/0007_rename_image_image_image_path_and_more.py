# Generated by Django 4.2.4 on 2023-08-11 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_num_pages_image_channels_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_path',
        ),
        migrations.RenameField(
            model_name='pdf',
            old_name='pdf',
            new_name='pdf_path',
        ),
    ]