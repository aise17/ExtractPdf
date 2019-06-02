from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer

from .models import AnuncioLateral, AnuncioInferior, AnuncioSuperior, Bono, Explicacion, QuienSomos, Faqs, \
    ExplicacionScrapy, NormasScrapy, NormasOcr
from .serializers import AnuncioLateralSerializer, AnuncioInferiroSerializer, \
    AnuncioSuperiorSerializer, BonoSerializer, ExplicaionSerializer, QuienSomosSerializer, FaqsSerializer, \
    ExplicaionScrapySerializer

from rest_framework.response import Response
from rest_framework import status

import sys
sys.path.append('../')

from ocr_api.utils import servicioTraza



def procesarSalidaContenido(serializer_class, queryset):
    salida = dict()

    ser = serializer_class(queryset.all(), many=True)

    salida['salida'] = ser.data

    if salida['salida'].__len__() is queryset.all().__len__():
        salida['ok'] = True
    else:
        salida['ok'] = False
        salida['error'] = 'Fallo en la serializacion de archivos'

    return salida



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

    def get(self, request, *args, **kwargs):
        '''
        get:
        Return one list of bono's availables
        '''

        salida = procesarSalidaContenido(self.get_serializer_class(), self.get_queryset())

        servicioTraza(request, salida, FaqsView.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class FaqsView(generics.ListAPIView):
    queryset = Faqs.objects.filter(publicado=True).order_by('fecha_publicacion')
    serializer_class = FaqsSerializer

    def get(self, request, *args, **kwargs):
        '''
        get:
        Return one list of bono's availables
        '''

        salida = procesarSalidaContenido(self.get_serializer_class(), self.get_queryset())

        servicioTraza(request, salida, FaqsView.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class BonosView(generics.ListAPIView):
    queryset = Bono.objects.filter(activado=True).order_by('precio')
    serializer_class = BonoSerializer

    def get(self, request, *args, **kwargs):
        '''
        get:
        Return one list of bono's availables
        '''

        salida = procesarSalidaContenido(self.get_serializer_class(), self.get_queryset())

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

    def get(self, request, *args, **kwargs):
        '''
        get:
        Return one list of bono's availables
        '''

        salida = procesarSalidaContenido(self.get_serializer_class(), self.get_queryset())

        servicioTraza(request, salida, FaqsView.__name__)

        return Response(salida, status=status.HTTP_200_OK)




@permission_classes([AllowAny])
class ExplicacionScrapyView(generics.ListAPIView):
    '''
    get:
    Return a list of contents for index page. These will try to explain the contents of the services
    '''
    queryset = ExplicacionScrapy.objects.filter(publicado=True).order_by('fecha_publicacion')[:3]
    serializer_class = ExplicaionScrapySerializer

    def get(self, request, *args, **kwargs):
        '''
        get:
        Return one list of bono's availables
        '''

        salida = procesarSalidaContenido(self.get_serializer_class(), self.get_queryset())

        servicioTraza(request, salida, FaqsView.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class NormasOcrView(generics.ListAPIView):
    '''
    get:
    Return a list of contents for index page. These will try to explain the contents of the services
    '''
    queryset = NormasOcr.objects.filter(publicado=True).order_by('fecha_publicacion')[:3]
    serializer_class = ExplicaionScrapySerializer

    def get(self, request, *args, **kwargs):
        '''
        get:
        Return one list of bono's availables
        '''

        salida = procesarSalidaContenido(self.get_serializer_class(), self.get_queryset())

        servicioTraza(request, salida, FaqsView.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class NormasScrapyView(generics.ListAPIView):
    '''
    get:
    Return a list of contents for index page. These will try to explain the contents of the services
    '''
    queryset = NormasScrapy.objects.filter(publicado=True).order_by('fecha_publicacion')[:3]
    serializer_class = ExplicaionScrapySerializer

    def get(self, request, *args, **kwargs):
        '''
        get:
        Return one list of bono's availables
        '''

        salida = procesarSalidaContenido(self.get_serializer_class(), self.get_queryset())

        servicioTraza(request, salida, FaqsView.__name__)

        return Response(salida, status=status.HTTP_200_OK)

@permission_classes([AllowAny])
class QuienesSomosView(generics.ListAPIView):
    '''
    get:
    Returns content to let us know as developers
    '''
    queryset = QuienSomos.objects.filter(publicado=True)
    serializer_class = QuienSomosSerializer

    def get(self, request, *args, **kwargs):
        '''
        get:
        Return one list of bono's availables
        '''

        salida = procesarSalidaContenido(self.get_serializer_class(), self.get_queryset())

        servicioTraza(request, salida, FaqsView.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class AndroidIndex(generics.ListAPIView):
    queryset = [{
        "relation": ["delegate_permission/common.handle_all_urls"],
        "target": {
            "namespace": "android_app",
            "package_name": "com.juanfe.withapi",
            "sha256_cert_fingerprints":
            ["99:50:A3:1B:E3:8D:32:44:A1:94:91:49:36:CA:07:9E:78:54:05:35:95:0C:B2:78:5D:D2:5D:0A:D1:17:ED:06"]
        }
        }]

    def get(self, request, *args, **kwargs):
        salida = self.get_queryset()
        servicioTraza(request, salida, FaqsView.__name__)

        return Response(salida, status=status.HTTP_200_OK)

