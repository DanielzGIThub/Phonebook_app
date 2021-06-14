# Phonebook_app - phbook
This is a simple app storing email addresses and phone numbers created using Django 2.2.5

In order to configure it please follow these instructions:

### just after you clone the repository to your directory:
```
  $cd Phonebook_app
  pip3 install virtualenv
  virtualenv -p python3 env
  source env/bin/activate (depends on env, just check your env installed, something like '$env/Scripts/activate.bat')
  pip install -r requirements.txt
  python3 manage.py makemigrations phbook (or python instead of python3, depends on your enviroment variables)
  python3 manage.py migrate
  python3 manage.py runserver
```
url main page: phbook/index
