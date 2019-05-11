from django.shortcuts import render
import sys


sys.path.append("..")

from seguridad.models import MinSizeDocumento
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class IsAuthenticatedOrPost(IsAuthenticated):
    def has_permission(self, request, view):

        print('[+][+][+] el docuemto pesa -> {} '.format(request.data.get('documento').size))

        regla =  MinSizeDocumento.objects.get(activo=True)

        if super().has_permission(request, view):
            return True

        if request.data.get('documento').size < regla.tam_min:
            return True
        #return super().has_permission(request, view)

