from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer

from .models import AnuncioLateral, AnuncioInferior, AnuncioSuperior, Bono, Explicacion, QuienSomos, Faqs
from .serializers import AnuncioLateralSerializer, AnuncioInferiroSerializer, \
    AnuncioSuperiorSerializer, BonoSerializer, ExplicaionSerializer, QuienSomosSerializer, FaqsSerializer

from rest_framework.response import Response
from rest_framework import status

import sys
sys.path.append('../')

from ocr_api.utils import servicioTraza

@permission_classes([AllowAny])
class AnuncioSuperiroView(generics.ListAPIView):
    '''
    get:
    Return a script provided by GoogleAdwords
    '''
    queryset = AnuncioSuperior.objects.filter(publicado=True)
    serializer_class = AnuncioSuperiorSerializer

@permission_classes([AllowAny])
class AnuncioInferiorView(generics.ListAPIView):
    '''
    get:
    Return a script provided by GoogleAdwords
    '''
    queryset = AnuncioInferior.objects.filter(publicado=True)
    serializer_class = AnuncioInferiroSerializer

@permission_classes([AllowAny])
class AnuncioLateralView(generics.ListAPIView):
    '''
    get:
    Return a script provided by GoogleAdwords
    '''
    queryset = AnuncioLateral.objects.filter(publicado=True)
    serializer_class = AnuncioLateralSerializer


@permission_classes([AllowAny])
class FaqsView(generics.ListAPIView):
    queryset = Faqs.objects.filter(activado=True).order_by('precio')
    serializer_class = FaqsSerializer

    def get(self, request, *args, **kwargs):
        '''
        get:
        Return one list of bono's availables
        '''

        salida = dict()

        ser = FaqsSerializer(self.queryset.all(), many=True)

        salida['salida'] = ser.data

        if salida['salida'].__len__() is self.queryset.all().__len__():
            salida['ok'] = True
        else:
            salida['ok'] = False
            salida['error'] = 'Fallo en la serializacion de archivos'

        servicioTraza(request, salida, FaqsView.__name__)

        return Response(salida, status=status.HTTP_200_OK)




# Todo


@permission_classes([AllowAny])
class BonosView(generics.ListAPIView):
    queryset = Bono.objects.filter(activado=True).order_by('precio')
    serializer_class = BonoSerializer

    def get(self, request, *args, **kwargs):
        '''
        get:
        Return one list of bono's availables
        '''

        salida = dict()

        ser = BonoSerializer(self.queryset.all(), many=True)

        salida['salida'] = ser.data

        if salida['salida'].__len__() is self.queryset.all().__len__():
            salida['ok'] = True
        else:
            salida['ok'] = False
            salida['error'] = 'Fallo en la serializacion de archivos'

        servicioTraza(request, salida, BonosView.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class ExplicacionInicio(generics.ListAPIView):
    '''
    get:
    Return a list of contents for index page. These will try to explain the contents of the services
    '''
    queryset = Explicacion.objects.filter(publicado=True).order_by('fecha_publicacion')[:3]
    serializer_class = ExplicaionSerializer

@permission_classes([AllowAny])
class QuienesSomosView(generics.ListAPIView):
    '''
    get:
    Returns content to let us know as developers
    '''
    queryset = QuienSomos.objects.filter(publicado=True)
    serializer_class = QuienSomosSerializer