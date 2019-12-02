from django.shortcuts import render, redirect
#importar mi modelo
from .models import Registro
#importar modelo de usuarios django
from django.contrib.auth.models import User


# registrar usuarios
def registrar(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        contra = request.POST['contra']
        print(nombre,email,contra)
        user = User.objects.create_user(nombre,email,contra)
        user.is_staff = True;
        user.save()
        redirect('index')
    return render(request, 'registro.html')
