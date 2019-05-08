from django.shortcuts import render
import sys

sys.path.append("..")

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from ocr_api.serializers import ArchivoSerializer


class IsAuthenticatedOrPost(IsAuthenticated):
    def has_permission(self, request, view):

        print("[+][+] el peso del documento recivido es de {}->".format(request.data.get('documento').size))

        if request.data.get('documento').size < 20000:
            return True
        return super().has_permission(request, view)