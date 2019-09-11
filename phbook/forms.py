from django.forms import ModelForm
from django import forms
from .models import Person, Phonenumber

class PersonAdd(ModelForm):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname']
