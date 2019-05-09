from django.shortcuts import render
import sys

sys.path.append("..")

# Create your views here.
from rest_framework.permissions import IsAuthenticated


class IsAuthenticatedOrPost(IsAuthenticated):
    def has_permission(self, request, view):

        try:
            if request.data.get('documento').count:
                return True
        except:
            if request.data.get('documento').size < 20000:
                return True
        return super().has_permission(request, view)

