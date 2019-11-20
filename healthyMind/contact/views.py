from django.shortcuts import render
# Importar del fichero de formularios
from .forms import form
#Vista para los Contactos
def contacto(request):
    #instanciar el formulario y guardarlo en una variable
    formulario = form()
    return render(request, 'contact/contactoMind.html', {'formulario': formulario})#Indicar el diccionario de contexto ({}) para enviarlo al template.
