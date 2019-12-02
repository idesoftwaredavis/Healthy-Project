# Generated by Django 2.2 on 2019-11-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('contrasenia', models.CharField(max_length=50, verbose_name='Contraseña')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
    ]
