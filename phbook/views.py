from django.shortcuts import render, get_object_or_404, redirect
from .models import Person, Email, Phonenumber
from django.views import generic
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .forms import PersonAdd


def personslist(request):
    allpersons = Person.objects.all().order_by('lastname')
    return render(request, 'index.html', {'allpersons': allpersons})


class SearchByPerson(generic.ListView):
    model = Person
    template_name = 'searchresults.html'
    context_object_name = 'allpersons'
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Person.objects.filter(
            Q(firstname__icontains=query) | Q(lastname__icontains=query) 
            | Q(email__email__contains=query) | Q(phonenumber__phonenumber__contains=query)
            ).distinct().order_by('lastname')
        return object_list


def add_person(request):
    form = PersonAdd(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(personslist)
    return render(request, 'addperson.html', {'form' : form})


def edit_person(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonAdd(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect(personslist)
    return render(request, 'addperson.html', {'form' : form})


def del_person(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'POST':
        person.delete()
        return redirect(personslist)
    return render(request, 'delconfirm.html', {'person' : person})


@csrf_exempt
def add_phone(request, id):
    if request.method == 'POST':
        id = request.POST.get('id')
        phone = request.POST.get('phone')
        person = Person.objects.get(pk=id)
        person.phonenumber_set.create(phonenumber=phone)
        return redirect(personslist)
    return render(request, 'addphone.html', {'id' : id})


@csrf_exempt
def add_email(request, id):
    if request.method == 'POST':
        id = request.POST.get('id')
        email = request.POST.get('email')
        person = Person.objects.get(pk=id)
        person.email_set.create(email=email)
        return redirect(personslist)
    return render(request, 'addemail.html', {'id' : id})
