# Generated by Django 4.2.4 on 2023-08-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('location', models.URLField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('channels', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='pdfs')),
                ('location', models.URLField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('number_pages', models.IntegerField()),
            ],
            options={
                'verbose_name': 'PDF',
                'verbose_name_plural': 'PDFs',
            },
        ),
    ]
