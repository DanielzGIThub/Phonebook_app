from django.urls import path, include
from . import views


urlpatterns = [
    path('index/', views.personslist, name='index'),
    path('search/', views.SearchByPerson.as_view(), name='search_results'),
    path('addperson/', views.add_person, name='add_person'),
    path('editperson/<int:id>/', views.edit_person, name='edit_person'),
    path('delperson/<int:id>/', views.del_person, name='del_person'),
    path('addphone/<int:id>/', views.add_phone, name='add_phone'),
    path('addemail/<int:id>/', views.add_email, name='add_email'),
]
