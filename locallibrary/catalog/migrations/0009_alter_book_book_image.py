# Generated by Django 4.1 on 2022-11-16 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_author_author_image_book_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, default='book_default.jpg', null=True, upload_to=''),
        ),
    ]
