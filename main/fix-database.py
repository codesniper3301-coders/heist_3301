from os import system
system('python manage.py makemigrations')
system('python manage.py migrate')
print('\n\n\n create admin account')
system('python manage.py createsuperuser')
system('.\startserver.py')