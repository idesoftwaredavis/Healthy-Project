# Generated by Django 2.2 on 2019-11-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20191119_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=5, verbose_name='Precio'),
        ),
    ]
