from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import formBook, formStore, autorForm, storeform
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
# Create your views here.
#Vista para los E-ebooks

#funcion para listar todos los libros
def ebooks(request):
    libro = Book.objects.all()
    return render(request, 'store/ebooks.html',{'libro': libro})

#funcion para listar libro
def listEbookById(request, id):
    book = Book.objects.filter(id=id)
    print(book)
    return render(request, 'store/detalle.html', {'book': book})


#funcion para eliminar libro (Vistas basadas en funciones)
def deleteBookById(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('ebooks')
    return render (request, 'store/eliminarLibro.html', {'book': book})


#funcion para crear libro (Vistas basadas en funciones)
def createBook(request):
    model  = storeform(request.POST, request.FILES)
    #verificacion si es metodo POST
    if request.method == 'POST':
        if model.is_valid():
            model.save()
            return redirect('ebooks')
    else:
        model = storeform()
    return render(request, 'store/crearLibro.html', {'modelBook': model})

#Actualizar libro (Utilizando vistas basadas en clases)
def actualizarLibro(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'GET':
        form = storeform(instance=book)
    else:
        form = storeform(request.POST,request.FILES, instance=book)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'store/modificarLibro.html', {'form': form})
