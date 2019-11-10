from django.urls import path
#Importamos el archivo .py 'views', para hacer el llamado de los TEMPLATES
from . import views
# Ingreso de todos los path correspondientes a la app 'main'

urlpatterns=[
    path('', views.registro, name = "registro"),
    path('', views.articulos, name = "articulos"),
    path('', views.ebooks, name = "ebooks"),
    path('', views.contacto, name = "contacto"),
]
