from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length = 50, verbose_name = "Nombre")
    email = models.EmailField(max_length = 50, verbose_name = "Email", null = False)
    contrasenia = models.CharField(max_length=50, verbose_name = "Contraseña")

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return self.nombre
