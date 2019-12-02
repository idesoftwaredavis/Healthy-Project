from django.urls import path
#Importamos el archivo .py 'views', para hacer el llamado de los TEMPLATES
from . import views
# Ingreso de todos los path correspondientes a la app 'main'

urlpatterns=[
    path('Ebooks/', views.ebooks, name = "ebooks"),
    path('detalle/<int:id>/', views.listEbookById, name = "detalle"),
    path('eliminar/<int:id>/', views.deleteBookById, name = "delete"),
    path('create', views.createBook, name = "create"),
    path('actualizar/<int:id>', views.actualizarLibro, name = "actualizar")
]
