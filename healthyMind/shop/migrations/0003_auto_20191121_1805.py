# Generated by Django 2.2 on 2019-11-21 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20191121_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='shop', verbose_name='imagen'),
        ),
    ]
