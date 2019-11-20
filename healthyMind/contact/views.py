from django.shortcuts import render, redirect
# Importar del fichero de formularios
from .forms import form, formContact
#Vista para los Contactos
def contacto(request):
    #instanciar el formulario y guardarlo en una variable
    formulario = form()
    return render(request, 'contact/contactoMind.html', {'formulario': formulario})#Indicar el diccionario de contexto ({}) para enviarlo al template.

# crear contacto (VISTA BASADA EN FUNCION)
def createContact(request):
    #Protocolo Http - Interacción -> POST (Enviarle datos al servidor para guardarlo) - GET (Aquel que se llama cuando queremos utilizar informacion del servidor)

    # pregunto si se trata de una peticion POST, para poder registrar los datos de contacto en la Basde de Datos healthybd
    if request.method == 'POST':
        #instancia form() y recibe los datos desde request.POST . guardo en variable form_contact para que cree contenido html.
        data = request.POST
        form_contact = formContact(request.POST)
        #estructura condicional para asegurar que los datos son correctos con metodo interno is_valid().
        if form_contact.is_valid():
            #metodo save() que guarda los request.POST en el cual contiene todos los campos con informacion del Cliente para ser guardados.
            form_contact.save()
            # indicar al usuario el exito/error de la operacion realizada.
            return redirect('index')
    else:
        #Si el protocolo es GET, se realiza el form de manera limpia
        form_contact = formContact()
        print(form_contact)
        #Retorno el template contactoMind.html, indicandole con diccionario de contexto, el form.
    return render(request, 'contact/contactoMind.html', {'formulario': form_contact})
