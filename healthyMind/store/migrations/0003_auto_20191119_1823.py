# Generated by Django 2.2 on 2019-11-19 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20191119_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=250, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='book',
            name='short_description',
            field=models.TextField(max_length=250, verbose_name='Descripcion Corta'),
        ),
    ]