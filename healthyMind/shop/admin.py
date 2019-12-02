from django.contrib import admin
from .models import Author, Book
# Register your models here.
#Registrar modelo Author a django Administrator
admin.site.register(Author)
#Registrar modelo book a django Administrator
admin.site.register(Book)
