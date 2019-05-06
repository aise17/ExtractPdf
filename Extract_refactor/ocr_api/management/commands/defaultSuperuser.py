

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Crea superadministrador'

    def handle(self, *args, **options):

        if(User.objects.filter(username='admin')):
            print('[+] El usuario superadministrador ya existe')

        else:

            user = User()
            user.username('admin')
            user.set_password('admin')
            user.is_superuser = True
            user.is_staff = True

            user.save()

            print('[+] superadministrador creado')
