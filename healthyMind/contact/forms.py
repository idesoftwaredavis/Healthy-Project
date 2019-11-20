from django import forms
from .models import contact
class formContact(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
