from django.shortcuts import render
# Aca se crean las vistas para despues ser llamadas desde el urls.py


# Vista para el Registro
def registro(request):
    return render (request, 'principal/Registro/registro.html')


#Vista para los articulos
def articulos(request):
    return render(request, 'principal/Articulos/article1.html')




# vista index
def index (request):
    return render(request, 'principal/index.html')
