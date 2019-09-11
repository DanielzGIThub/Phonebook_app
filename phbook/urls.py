from django.urls import path, include
from . import views


urlpatterns = [
    path('index/', views.personlist1, name='index'),
    path('addperson/', views.add_person, name='addperson'),
    path('editperson/<int:id>/', views.edit_person, name='edit_person'),
    path('delperson/<int:id>/', views.del_person, name='del_person'),
    path('response/', views.del_person, name='response'),
    path('search/', views.SearchByPerson.as_view(), name='search_results'),
    path('addphone/<int:id>/', views.phoneadd, name='add_phone'),
    path('addemail/<int:id>/', views.emailadd, name='add_email'),
    path('testphone/', views.phonesave, name='testphone'),
    path('testemail/', views.emailsave, name='testemail'),
]
    
'''
    path('all/', all_persons),
    path('addperson/', add_person, name='addperson'),
    path('editperson/<int:id>/', edit_person, name='edit_person'),
    path('delperson/<int:id>/', del_person, name='del_person'),
    path('addphone/<int:id>/', add_phone, name='add_phone'),
    path('addemail/<int:id>/', add_email, name='add_email'),'''
