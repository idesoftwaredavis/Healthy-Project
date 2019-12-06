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
        registro = Registro(nombre=nombre,email=email,contrasenia=contra)
        registro.save()
        user.is_staff = True;
        user.save()
        return redirect('index')
    return render(request, 'registro.html')

def login (request):
    return render(request, 'login/login.html')

#validar usuario
def validaUsuario(request):
    try:
        user = request.POST['usuario']
        contra = request.POST['pass']
        #solamente para prueba
        print(user, contra)
        validarNombre = Registro.objects.filter(nombre__exact = user).get()
        validarContra = Registro.objects.filter(contrasenia__exact = contra).get()
        print (validarContra.nombre)
        if  contra == validarContra.contrasenia and user == validarNombre.nombre:
            return render(request,'principal/index.html')
        else:
            return render(request,'login/login.html')
    except:
        mensaje = "usuario o contrasenia incorrectas"
        return render (request, 'login/login.html',{'mensaje':mensaje})
