from django.db import models

class contact(models.Model):
    nombres = models.CharField(verbose_name="nombre", blank = False, null = False, max_length= 50)
    apellidos = models.CharField(verbose_name="apellidos", blank = False, null = False, max_length = 50)
    email = models.EmailField(verbose_name = "Email", blank = True, null = True, max_length = 50)
    mensaje = models.CharField(verbose_name="mensaje", blank = False, null = False, max_length = 250)

    choices_contact = (
        ('Desarrollo Personal', 'Desarrollo Personal'),
        ('Bienestar Personal', 'Bienestar Personal'),
        ('Curso Meditacion', 'Curso Meditacion')
    )

    title = models.CharField(max_length=100, choices = choices_contact)

    class Meta:
        verbose_name = "contacto"
        verbose_name_plural = "contactos"

    def __str__(self):
        return 'contacto de %s' % (self.nombres)
