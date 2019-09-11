from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Person, Email, Phonenumber
from django.views import generic
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .forms import PersonAdd
from django.contrib.auth.decorators import login_required


def personlist1(request):
    allpersons = Person.objects.all().order_by('lastname')
    context = {'allpersons': allpersons}

    return render(request, 'index.html', context)


class SearchByPerson(generic.ListView):
    model = Person
    template_name = 'searchresults.html'
    context_object_name = 'allpersons'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Person.objects.filter(
            Q(firstname__icontains=query) | Q(lastname__icontains=query) | Q(email__email__contains=query) | Q(phonenumber__phonenumber__contains=query)
        ).distinct()
        return object_list

#@login_required
def add_person(request):
    form = PersonAdd(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(personlist1)
    return render(request, 'new_person.html', {'form' : form})

#@login_required
def edit_person(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonAdd(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect(personlist1)
    return render(request, 'new_person.html', {'form' : form})

#@login_required
def del_person(request, id):
    person = get_object_or_404(Person, pk=id)
    pname =str(person.firstname) + ' ' + str(person.lastname)
    if len(person.email_set.all())==0 and len(person.phonenumber_set.all())==0:
        if request.method == 'POST':
            person.delete()
            return redirect(personlist1)
    else:
        return render(request, 'responsepage.html', {'pname': pname})
    
    return render(request, 'confirm.html', {'person' : person, 'pname': pname})

'''
def response(request):
    pname =str(person.firstname) + ' ' + str(person.lastname)
    return render(request, 'response.html', {'pname': pname})'''

@csrf_exempt
def email(request):
    #id = request.POST.get('id')
    #return render(request, 'test.html', {'id': id})
    id = request.POST.get('id')
    email = request.POST.get('email')
    person = Person.objects.get(pk=id)
    person.email_set.create(email=email)
    return redirect(personlist1)

'''
@csrf_exempt
def phone(request):
    #id = request.POST.get('id')
    #return render(request, 'test.html', {'id': id})
    id = request.POST.get('id')
    phone = request.POST.get('phone')
    person = Person.objects.get(pk=id)
    person.phonenumber_set.create(phonenumber=phone)
    return redirect(personlist1)
'''

#@login_required
def phoneadd(request, id):
    #id = request.POST.get('id')
    return render(request, 'addphone.html', {'id' : id})

@csrf_exempt
def phonesave(request):
    id = request.POST.get('id')
    phone = request.POST.get('phone')
    person = Person.objects.get(pk=id)
    person.phonenumber_set.create(phonenumber=phone)
    return redirect(personlist1)

#@login_required
def emailadd(request, id):
    #id = request.POST.get('id')
    return render(request, 'addemail.html', {'id' : id})

@csrf_exempt
def emailsave(request):
    id = request.POST.get('id')
    email = request.POST.get('email')
    person = Person.objects.get(pk=id)
    person.email_set.create(email=email)
    return redirect(personlist1)