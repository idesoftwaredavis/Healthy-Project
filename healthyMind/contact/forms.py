from django import forms
from .models import contact



class formContact(forms.ModelForm):
    class Meta:
        model = contact
        fields =['nombres','apellidos','email','mensaje','title']

class form (forms.Form):
    choices_contact = (
        ('Desarrollo Personal', 'Desarrollo Personal'),
        ('Bienestar Personal', 'Bienestar Personal'),
        ('Curso Meditacion', 'Curso Meditacion')
    )
    nombres = forms.CharField(label = "Nombres", required= True, widget = forms.TextInput(attrs={'class':'form-control'}))
    apellidos = forms.CharField(label = "Apellidos", required= True, widget = forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label = "Email", required= True, widget = forms.TextInput(attrs={'class':'form-control'}))
    mensaje = forms.CharField(label = "Mensaje", required= True, widget = forms.Textarea(attrs={'class':'form-control'}))

    cbxContact = forms.CharField(
        max_length=100,
        widget=forms.Select(choices=choices_contact, attrs= {'class':'form-control'}),
    )
