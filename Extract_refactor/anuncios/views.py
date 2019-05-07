from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from .models import AnuncioLateral, AnuncioInferior, AnuncioSuperior
from .serializers import AnuncioLateralSerializer, AnuncioInferiroSerializer, \
    AnuncioSuperiorSerializer


@permission_classes([AllowAny])
class AnuncioSuperiroView(generics.ListCreateAPIView):
    queryset = AnuncioSuperior.objects.filter(publicado=True).order_by('fecha_publicacion')[:1]
    serializer_class = AnuncioSuperiorSerializer

@permission_classes([AllowAny])
class AnuncioInferiorView(generics.ListCreateAPIView):
    queryset = AnuncioInferior.objects.filter(publicado=True).order_by('fecha_publicacion')[:1]
    serializer_class = AnuncioInferiroSerializer

@permission_classes([AllowAny])
class AnuncioLateralView(generics.ListCreateAPIView):
    queryset = AnuncioLateral.objects.filter(publicado=True).order_by('fecha_publicacion')[:1]
    serializer_class = AnuncioLateralSerializer