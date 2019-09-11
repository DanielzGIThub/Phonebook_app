from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='Imię')
    lastname = models.CharField(max_length=50, verbose_name='Nazwisko')

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Phonenumber(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=50)

    def __str__(self):
        return self.phonenumber

class Email(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.email

