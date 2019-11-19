from django.urls import path
#Importamos el archivo .py 'views', para hacer el llamado de los TEMPLATES
from . import views
# Ingreso de todos los path correspondientes a la app 'main'

urlpatterns=[
    path('Registro/', views.registro, name = "registro"),
    path('Articulos/', views.articulos, name = "articulos"),
    path('Contacto/', views.contacto, name = "contacto"),
    path('', views.index, name = "index")
]
