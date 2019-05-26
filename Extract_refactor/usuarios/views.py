import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework import generics, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.serializers import serialize

from .serializers import ArchivoSerializer, UserSerializer, IpsFileSerializers, IncidenciaSerializers, \
    BonoUsuarioSerializer
from .models import Incidencia, BonoUsuario

import sys
sys.path.append("..")

from usuarios.utils import eliminarToken
from ocr_api.models import File, IpsFiles
from ocr_api.utils import servicioTraza


from django.core.mail import EmailMessage



# Create your views here.
@permission_classes([AllowAny])
class RegisterUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def crear(self, request, *args, **kwargs):
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
class LogoutUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def logout(self, request, *args, **kwargs):
        salida = dict()

        if eliminarToken(request):
            salida['ok'] = True
        else:
            salida['ok'] = False
            salida['error'] = 'fallo en la desconexion'

        servicioTraza(request, salida, LogoutUser.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class UserDetail(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def userDetail(self, request, *args, **kwargs):
        salida = dict()

        user = User.objects.get(id=request.data.get('id'))

        user = self.serializer_class().update(instance=user, validated_data=request.data)

        if user is not None:
            salida['ok'] = True
            salida['user'] = user
        else :
            salida['ok'] = False
            salida['error'] = self.serializer_class.error_messages

        servicioTraza(request, salida, UserDetail.__name__)

        return Response(salida, status=status.HTTP_200_OK)

@permission_classes([AllowAny])
class AuthentificacionUsuario(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def login(self, request, *args, **kwargs):
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
class RequestProcessOcrByUser(viewsets.ModelViewSet):
    queryset = IpsFiles.objects.filter(fecha_conexion__year=datetime.date.today().year)
    serializer_class = IpsFileSerializers

    def userStadisticRequest(self, request, *args, **kwargs):
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
class BonosComprodosbyYear(viewsets.ModelViewSet):
    queryset = BonoUsuario.objects.filter(fecha_creacion__year=datetime.date.today().year)
    serializer_class = BonoUsuarioSerializer

    def bonosConpardosbyYear(self, request, *args, **kwargs):
        salida = dict()

        if len(self.queryset) > 0:

            salida['ok'] = True

            salida['enero'] = len(self.queryset.filter(fecha_creacion__month='01'))
            salida['febrero'] = len(self.queryset.filter(fecha_creacion__month='02'))
            salida['marzo'] = len(self.queryset.filter(fecha_creacion__month='03'))
            salida['abril'] = len(self.queryset.filter(fecha_creacion__month='04'))
            salida['mayo'] = len(self.queryset.filter(fecha_creacion__month='05'))
            salida['junio'] = len(self.queryset.filter(fecha_creacion__month='06'))
            salida['julio'] = len(self.queryset.filter(fecha_creacion__month='07'))
            salida['agosto'] = len(self.queryset.filter(fecha_creacion__month='08'))
            salida['septiembre'] = len(self.queryset.filter(fecha_creacion__month='09'))
            salida['octubre'] = len(self.queryset.filter(fecha_creacion__month='10'))
            salida['noviembre'] = len(self.queryset.filter(fecha_creacion__month='11'))
            salida['diciembre'] = len(self.queryset.filter(fecha_creacion__month='12'))

        else:
            salida['ok'] = False
            salida['error'] = 'fallo en la optencion del usuario'

        servicioTraza(request, salida, RequestProcessOcrByUser.__name__)

        return Response(salida, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class FilesForUser(viewsets.ModelViewSet):
    serializer_class = ArchivoSerializer

    def get_object(self):
        if self.request.data.get('username'):
            return File.objects.filter(usuario__username=self.request.data.get('username'))
        else:
            return File.objects.filter(usuario=None)

    def getFilesForUser(self, request, *args, **kwargs):
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
class ContactoView(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializers

    def sendCommunication(self, request, *args, **kwargs):
        salida = dict()
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

        return Response(salida, status=status.HTTP_201_CREATED)


@permission_classes([AllowAny])
class BonosShop(viewsets.ModelViewSet):
    queryset = BonoUsuario.objects.all()
    serializer_class = BonoUsuarioSerializer



    def shopUserBonus(self, request, *args, **kwargs):
        salida = dict()

        bono_usuario = BonoUsuarioSerializer(data=request.data)

        if bono_usuario.is_valid():
            bono_usuario.save()
            salida['ok'] = True

        else:
            salida['ok'] = False
            salida['error'] = bono_usuario.error_messages

        servicioTraza(request, salida, BonosByUserListView.__name__)


        return Response(salida, status=status.HTTP_201_CREATED)

@permission_classes([AllowAny])
class BonosByUserListView(viewsets.ModelViewSet):
    queryset = BonoUsuario.objects.all()
    serializer_class = BonoUsuarioSerializer

    def getUserBonus(self, request, *args, **kwargs):
        salida = dict()


        user = User.objects.get(id=request.data.get('usuario'))
        print('[]þ]þ]þ] usuario {} '.format(request.data.get('usuario')))
        bonos = self.queryset.filter(usuario=user)

        ser = BonoUsuarioSerializer(bonos, many=True)


        if bonos is not None:
            salida['ok'] = True
            salida['salida'] = ser.data
        else:
            salida['ok'] = False
            salida['error'] = 'fallo al obtener usuario'

        servicioTraza(request, salida, BonosByUserListView.__name__)

        return Response(salida, status=status.HTTP_200_OK)
