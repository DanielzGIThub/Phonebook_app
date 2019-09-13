# Phonebook_app - phbook
This is a simple app storing email addresses and phone numbers created using Django 2.2.5

In order to configure it please follow these instructions:

### just after you clone the repository to your directory:
```
  $cd Phonebook_app
  pip3 install virtualenv
  virtualenv -p python3 env
  source env/bin/activate
  pip install -r requirements.txt
  python3 manage.py runserver
  python3 manage.py makemigrations phbook
  python3 manage.py migrate
```
url main page: phbook/index

### initial data fixtures:
```
  python3 manage.py loaddata /fixtures/persons.json
```
