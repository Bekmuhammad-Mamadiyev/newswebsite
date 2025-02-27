from .models import Contacts
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
