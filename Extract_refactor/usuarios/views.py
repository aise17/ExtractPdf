
import sys



sys.path.append("..")

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArchivoSerializer, UserSerializer, IpsFileSerializers, IncidenciaSerializers
from .models import Incidencia
from ocr_api.models import File, IpsFiles, Traza
from ocr_api.utils import servicioTraza


from django.core.mail import EmailMessage



# Create your views here.
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

        servicioTraza(request, salida, RegisterUser.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class LogoutUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        salida = dict()
        logout(request)
        salida['ok'] = True
        servicioTraza(request, salida, LogoutUser.__name__)
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

        servicioTraza(request, salida, UserDetail.__name__)

        return Response(salida, status=status.HTTP_200_OK)

@permission_classes([AllowAny])
class AuthentificacionUsuario(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        salida = dict()

        s = authenticate(username=request.data.get('usuario'), password=request.data.get('password'))
        if s is not None:
            login(request, s)
            salida['ok'] = True
            ser = UserSerializer(instance=s)
            salida['user'] = ser.data
        else:
            salida['ok'] = False

        #servicioTraza(request, salida, AuthentificacionUsuario)


        return Response(salida, status=status.HTTP_200_OK)


class RequestProcessOcrForUser(generics.ListCreateAPIView):

    serializer_class = IpsFileSerializers

    def get_object(self):
        return IpsFiles.objects.filter(usuario__username=self.request.data.get('username'))

    def post(self, request, *args, **kwargs):
        salida = dict()

        if request.data.get('id') is not None:

            salida['ok'] = True

            #TODO reemplazar las 12 consultas por una que contenga un array con todos los meses para luego iterar por el.
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

        servicioTraza(request, salida, RequestProcessOcrForUser.__name__)

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

        servicioTraza(request, salida, FilesForUser.__name__)

        return Response(salida, status=status.HTTP_200_OK)


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

        servicioTraza(request, salida, ContactoView.__name__)

        return Response(salida, status=status.HTTP_200_OK)
