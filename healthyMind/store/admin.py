from django.contrib import admin
from .models import Author, Book

#Registrar modelo Author a django Administrator
admin.site.register(Author)
#Registrar modelo book a django Administrator
admin.site.register(Book)
