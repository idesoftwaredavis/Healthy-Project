#Se realizan todos los modelos correspondientes a la app 'store'

# Import models de django.db
from django.db import models

# Clase Autor
class Author (models.Model):
    name = models.CharField(max_length = 50, blank = False, null = False, verbose_name = "Nombre")
    last_name = models.CharField(max_length = 50, blank = False, null = False, verbose_name = "Apellido")
    books = models.IntegerField()

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    #Retorna el nombre del autor en Django Administrator
    def __str__ (self):
        return self.name

# Clase Book
class Book (models.Model):
    title = models.CharField(max_length = 50, blank = False, null = False, verbose_name = "Titulo")
    short_description = models.TextField(max_length = 250, blank = False, null = False, verbose_name = "Descripcion Corta")
    description = models.TextField(blank = False, null = False, verbose_name = "Descripcion")
    published =models.DateTimeField(verbose_name = "Fecha Creacion")
    price = models.FloatField(verbose_name="Precio")
    quantity = models.IntegerField(verbose_name="Cantidad")
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Autor Libro")
    image = models.ImageField(verbose_name = "imagen", upload_to = "store", null = True) # campo para subir las imagenes de los libros

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.title
