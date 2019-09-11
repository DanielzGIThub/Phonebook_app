from django.contrib import admin
from .models import Person, Phonenumber, Email

admin.site.register(Person)
admin.site.register(Phonenumber)
admin.site.register(Email)