from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render

# Create your views here.

from rest_framework import generics, mixins
from rest_framework.decorators import permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArchivoSerializer, ExplicaionSerializer, AnuncioInferiroSerializer, AnuncioLateralSerializer, \
    AnuncioSuperiorSerializer, IncidenciaSerializers, UserSerializer, IpsFileSerializers, QuienSomosSerializer
from .models import File, AnuncioInferior, AnuncioSuperior, AnuncioLateral, Explicacion, Incidencia, IpsFiles, \
    QuienSomos
from django.http import HttpResponse, Http404

import sys

sys.path.append("../orc")

# from barModule.LectorTextoEnImagenes import main

from .tasks import orc

from ipware import get_client_ip

from django.contrib.gis.geoip2 import GeoIP2

from .utils import fileIpCreate


class FileView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = ArchivoSerializer




    def post(self, request, *args, **kwargs):
        if not request.data.get('id'):
            file_serializer = ArchivoSerializer(data=request.data)
            if file_serializer.is_valid():

                f = file_serializer.save()

                fileIpCreate(request, f)

                proceso = file_serializer.data.get('proceso')
                nombre: str = file_serializer.data.get('documento').__str__()
                nombre = nombre.split('/')[-1]

                # TODO leer proceso de los datos de entrada y configurar orc
                text = orc.delay(nombre, proceso)
        else:
            proceso = self.request.data.get('proceso')
            nombre: str = self.request.data.get('documento')
            text = orc.delay(nombre, proceso)


        text = text.get()

        # file_serializer.data

        salida = {
            "salida": text,
        }

        filename = nombre + '.txt'
        content = text
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        # return response

        return Response(salida, status=status.HTTP_201_CREATED)



@permission_classes([AllowAny])
class ExplicacionContent(generics.ListCreateAPIView):
    queryset = Explicacion.objects.filter(publicado=True).order_by('fecha_publicacion')[:3]
    serializer_class = ExplicaionSerializer

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

@permission_classes([AllowAny])
class ContactoView(generics.ListCreateAPIView):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializers

    def post(self, request, *args, **kwargs):
        incidencia = IncidenciaSerializers(data=request.data)
        if (incidencia.is_valid()):
            incidencia.save()

            email = EmailMessage(incidencia.data.get('asunto'), incidencia.data.get('contenido'),
                                 to=['sergio.martinez-g@hotmail.com'])
            email.send()

            salida = {
                'ok': 'true'
            }
        else:
            salida = {
                'ok': 'false'
            }
        return Response(salida, status=status.HTTP_200_OK)


class FilesForUser(generics.ListCreateAPIView):
    serializer_class = ArchivoSerializer

    def get_object(self):
        if (self.request.data.get('username')):
            return File.objects.filter(usuario__username=self.request.data.get('username'))
        else:
            return File.objects.filter(usuario=None)

    def post(self, request, *args, **kwargs):
        salida = dict()

        if request.data.get('id') is not None:

            salida['ok'] = True
            res = self.get_object()
            ser = ArchivoSerializer(res, many=True)
            salida['request'] = ser.data
        else:
            salida['ok'] = False
        return Response(salida, status=status.HTTP_200_OK)

class RequestProcessOcrForUser(generics.ListCreateAPIView):

    serializer_class = IpsFileSerializers

    def get_object(self):
        return IpsFiles.objects.filter(usuario__username=self.request.data.get('username'))

    def post(self, request, *args, **kwargs):
        salida = dict()

        if request.data.get('id') is not None:

            salida['ok'] = True
            #res = self.get_object()
            #ser = IpsFileSerializers(res, many=True)
            salida['enero'] = len(IpsFiles.objects.filter(fecha_conexion__month='01', usuario=request.data.get('id')))
            salida['febrero'] = len(IpsFiles.objects.filter(fecha_conexion__month='02', usuario=request.data.get('id')))
            salida['marzo'] = len(IpsFiles.objects.filter(fecha_conexion__month='03', usuario=request.data.get('id')))
            salida['abril'] = len(IpsFiles.objects.filter(fecha_conexion__month='04', usuario=request.data.get('id')))
            salida['mayo'] = len(IpsFiles.objects.filter(fecha_conexion__month='05', usuario=request.data.get('id')))
            salida['junio'] = len(IpsFiles.objects.filter(fecha_conexion__month='06', usuario=request.data.get('id')))
            salida['julio'] = len(IpsFiles.objects.filter(fecha_conexion__month='07', usuario=request.data.get('id')))
            salida['agosto'] = len(IpsFiles.objects.filter(fecha_conexion__month='08', usuario=request.data.get('id')))
            salida['septiembre'] = len(IpsFiles.objects.filter(fecha_conexion__month='09', usuario=request.data.get('id')))
            salida['octubre'] = len(IpsFiles.objects.filter(fecha_conexion__month='10', usuario=request.data.get('id')))
            salida['noviembre'] = len(IpsFiles.objects.filter(fecha_conexion__month='11', usuario=request.data.get('id')))
            salida['diciembre'] = len(IpsFiles.objects.filter(fecha_conexion__month='12', usuario=request.data.get('id')))


        else:
            salida['ok'] = False
        return Response(salida, status=status.HTTP_200_OK)


class RequestForMonth(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.filter(fecha_conexion__year=date.today().year, fecha_conexion__month=date.today().month)


class RequestForDay(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.filter(fecha_conexion=date.today())


class RequestForYear(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.filter(fecha_conexion__year=date.today().year)


class CoordenadasWithRequest(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.all()

    def get(self, request, *args, **kwargs):
        salida = []
        for ip in IpsFiles.objects.all():
            salida.append({'usuario': ip.usuario, 'lat': ip.lat, 'lon': ip.lon})
        return Response(salida, status=status.HTTP_200_OK)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        salida = dict()
        user = self.get_object()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            salida['ok'] = True
            salida['user'] = serializer.data
        else:
            salida['ok'] = False
        return Response(salida, status=status.HTTP_200_OK)

@permission_classes([AllowAny])
class AuthentificacionUsuario(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        salida = dict()

        s = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if s is not None:
            login(request, s)
            salida['ok'] = True
            ser = UserSerializer(instance=s)
            salida['user'] = ser.data
        else:
            salida['ok'] = False
        return Response(salida, status=status.HTTP_200_OK)

@permission_classes([AllowAny])
class LogoutUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        salida = dict()
        logout(request)
        salida['ok'] = True
        return Response(salida, status=status.HTTP_200_OK)

@permission_classes([AllowAny])
class QuienesSomos(generics.ListAPIView):
    queryset = QuienSomos.objects.filter(publicado=True).order_by('fecha_publicacion')[:1]
    serializer_class = QuienSomosSerializer

@permission_classes([AllowAny])
class RegisterUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        salida = dict()

        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            s = authenticate(username=request.data.get('username'), password=request.data.get('password'))
            if s is not None:
                login(request, s)
            salida['ok'] = True
            ser = UserSerializer(instance=s)

            salida['user'] = ser.data
        else:
            salida['ok'] = False

            salida['user'] = user.errors
        return Response(salida, status=status.HTTP_200_OK)

