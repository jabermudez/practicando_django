# Generated by Django 4.1.1 on 2022-09-10 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_imagen_referencia_post_imagen_referencial_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='imagen_referencia',
            new_name='imagen_referencial',
        ),
    ]
