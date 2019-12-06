from django.urls import path
#Importamos el archivo .py 'views', para hacer el llamado de los TEMPLATES
from . import views
# Ingreso de todos los path correspondientes a la app 'main'

urlpatterns=[
    path('Registro/', views.registrar, name = "registro"),
    path('valida', views.validaUsuario, name= 'validaUser'),
    path('login/', views.login, name ="login"),
]
