from django.shortcuts import render

# Aca se crean las vistas para despues ser llamadas desde el urls.py


# Vista para el Registro
def registro(request):
    return render (request, 'principal/Registro/registro.html')


#Vista para los articulos
def articulos(request):
    return render(request, 'principal/Articulos/article1.html')

#Vista para los E-ebooks
def ebooks(request):
    return render(request, 'principal/E-Books/ebooks.html')

#Vista para los Contactos
def contacto(request):
    return render(request, 'principal/contacto/contactoMind.html')
