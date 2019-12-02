from django import forms
from .models import Book, Author

class formBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class autorForm(forms.Form):
    book_author = forms.CharField(label ='ernesto', required= True, widget = forms.Select(attrs={'class':'form-control'}))


class formStore (forms.Form):

    title = forms.CharField(label = "Nombres", required= True, widget = forms.TextInput(attrs={'class':'form-control'}))
    short_description = forms.CharField(label = "Apellidos", required= True, widget = forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(label = "Email", required= True, widget = forms.Textarea(attrs={'class':'form-control'}))
    published = forms.DateField(label = "Publicacion", required= True, widget = forms.DateInput(attrs={'class':'form-control'}))
    price = forms.CharField(label = "Precio", required= True, widget = forms.NumberInput(attrs={'class':'form-control'}))
    quantity = forms.CharField(label = "Cantidad", required= True, widget = forms.NumberInput(attrs={'class':'form-control'}))
    #book_author = forms.CharField(label ='ernesto', required= True, widget = forms.Select(attrs={'class':'form-control'}))
    image = forms.CharField(label = 'imagen', required = True, widget = forms.FileInput(attrs={'class':'form-control'}) )


class storeform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','short_description','description','published','price','quantity','book_author','image']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'short_description': forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'published':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'book_author':forms.Select(attrs={'class':'form-control'}),
        }
