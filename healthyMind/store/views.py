from django.shortcuts import render
from .models import Book
# Create your views here.
#Vista para los E-ebooks
def ebooks(request):
    libro = Book.objects.all()
    return render(request, 'store/ebooks.html',{'libro': libro})
