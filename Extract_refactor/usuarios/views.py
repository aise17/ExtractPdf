
import sys



sys.path.append("..")

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.serializers import serialize

from .serializers import ArchivoSerializer, UserSerializer, IpsFileSerializers, IncidenciaSerializers, \
    BonoUsuarioSerializer
from .models import Incidencia, BonoUsuario
from ocr_api.models import File, IpsFiles
from ocr_api.utils import servicioTraza


from django.core.mail import EmailMessage



# Create your views here.
@permission_classes([AllowAny])
class RegisterUser(generics.CreateAPIView):
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

            salida['error'] = user.error_messages

        servicioTraza(request, salida, RegisterUser.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class LogoutUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        salida = dict()
        if logout(request):
            salida['ok'] = True
        else:
            salida['ok'] = False
            salida['error'] = 'fallo en la desconexion'

        servicioTraza(request, salida, LogoutUser.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class UserDetail(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def post(self, request, *args, **kwargs):
        salida = dict()

        user = User.objects.get(id=request.data.get('id'))
        user = self.serializer_class.update(user, request.data)

        if user is not None:
            salida['ok'] = True
            salida['user'] = user
        else :
            salida['ok'] = False
            salida['error'] = self.serializer_class.error_messages

        servicioTraza(request, salida, UserDetail.__name__)

        return Response(salida, status=status.HTTP_200_OK)

@permission_classes([AllowAny])
class AuthentificacionUsuario(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        salida = dict()

        s = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if s is not None:
            login(request, s)
            ser = UserSerializer(instance=s)



            salida['ok'] = True
            salida['salida'] = ser.data
        else:
            salida['ok'] = False
            salida['error'] = 'fallo en la autentificacion'

        servicioTraza(request, salida, AuthentificacionUsuario.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class RequestProcessOcrByUser(generics.CreateAPIView):
    queryset = IpsFiles.objects.all()
    serializer_class = IpsFileSerializers

    def post(self, request, *args, **kwargs):
        salida = dict()

        if request.data.get('id') is not None:

            salida['ok'] = True

            salida['enero'] = len(self.queryset.filter(fecha_conexion__month='01', usuario=request.data.get('id')))
            salida['febrero'] = len(self.queryset.filter(fecha_conexion__month='02', usuario=request.data.get('id')))
            salida['marzo'] = len(self.queryset.filter(fecha_conexion__month='03', usuario=request.data.get('id')))
            salida['abril'] = len(self.queryset.filter(fecha_conexion__month='04', usuario=request.data.get('id')))
            salida['mayo'] = len(self.queryset.filter(fecha_conexion__month='05', usuario=request.data.get('id')))
            salida['junio'] = len(self.queryset.filter(fecha_conexion__month='06', usuario=request.data.get('id')))
            salida['julio'] = len(self.queryset.filter(fecha_conexion__month='07', usuario=request.data.get('id')))
            salida['agosto'] = len(self.queryset.filter(fecha_conexion__month='08', usuario=request.data.get('id')))
            salida['septiembre'] = len(self.queryset.filter(fecha_conexion__month='09', usuario=request.data.get('id')))
            salida['octubre'] = len(self.queryset.filter(fecha_conexion__month='10', usuario=request.data.get('id')))
            salida['noviembre'] = len(self.queryset.filter(fecha_conexion__month='11', usuario=request.data.get('id')))
            salida['diciembre'] = len(self.queryset.filter(fecha_conexion__month='12', usuario=request.data.get('id')))


        else:
            salida['ok'] = False
            salida['error'] = 'fallo en la optencion del usuario'

        servicioTraza(request, salida, RequestProcessOcrByUser.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class FilesForUser(generics.CreateAPIView):
    serializer_class = ArchivoSerializer

    def get_object(self):
        if self.request.data.get('username'):
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
            salida['error'] = 'fallo en la identificacion'

        servicioTraza(request, salida, FilesForUser.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class ContactoView(generics.CreateAPIView):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializers

    def post(self, request, *args, **kwargs):
        salida = dict()
        usuario = User.objects.get()
        incidencia = IncidenciaSerializers(data=request.data)
        if (incidencia.is_valid()):

            i = incidencia.save()

            email = EmailMessage(incidencia.data.get('asunto'), incidencia.data.get('contenido'),
                                 to=['sergio.martinez-g@hotmail.com'])
            email.send()

            salida['ok'] = True
            salida['salida'] = incidencia.data
        else:
            salida['ok'] = False
            salida['error'] = incidencia.error_messages

        servicioTraza(request, salida, ContactoView.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class BonosByUserListView(generics.ListAPIView):
    queryset = BonoUsuario.objects.all()
    serializer_class = BonoUsuarioSerializer

    def get(self, request, *args, **kwargs):
        salida = dict()

        if request.data.get('usuarioId'):
            bonos = self.queryset.filter(usuario=request.data.get('usuarioId'))

            ser = BonoUsuarioSerializer(bonos, many=True)

            salida['ok'] = True
            salida['salida'] = ser.data
        else:
            salida['ok'] = False
            salida['error'] = 'fallo al obtener usuario'

        return Response(salida, status=status.HTTP_200_OK)


