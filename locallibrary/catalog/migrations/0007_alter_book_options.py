# Generated by Django 4.1.1 on 2022-10-14 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_author_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_edit_books', "Edit books' details"),)},
        ),
    ]