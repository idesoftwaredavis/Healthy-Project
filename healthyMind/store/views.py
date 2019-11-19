from django.shortcuts import render

# Create your views here.
#Vista para los E-ebooks
def ebooks(request):
    return render(request, 'store/ebooks.html')
