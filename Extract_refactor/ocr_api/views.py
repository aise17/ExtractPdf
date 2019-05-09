from datetime import date

from django.contrib.auth.models import User
from django.core.mail import EmailMessage


from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import sys

sys.path.append("..")

from seguridad.views import IsAuthenticatedOrPost
from .serializers import ArchivoSerializer, ExplicaionSerializer, IncidenciaSerializers, IpsFileSerializers, \
    QuienSomosSerializer, TrazaSerializer
from .models import File, Explicacion, Incidencia, IpsFiles, QuienSomos, Traza
from django.http import HttpResponse


from .tasks import orc

from ipware import get_client_ip

from django.contrib.gis.geoip2 import GeoIP2

from .utils import fileIpCreate, servicioTraza


@permission_classes([IsAuthenticatedOrPost])
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


        salida = {
            "salida": text,
        }

        servicioTraza(request, salida, FileView.__name__)

        return Response(salida, status=status.HTTP_201_CREATED)


@permission_classes([AllowAny])
class ExplicacionContent(generics.ListCreateAPIView):
    queryset = Explicacion.objects.filter(publicado=True).order_by('fecha_publicacion')[:3]
    serializer_class = ExplicaionSerializer



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

        servicioTraza(request, salida, CoordenadasWithRequest.__name__)

        return Response(salida, status=status.HTTP_200_OK)




@permission_classes([AllowAny])
class QuienesSomos(generics.ListAPIView):
    queryset = QuienSomos.objects.filter(publicado=True).order_by('fecha_publicacion')[:1]
    serializer_class = QuienSomosSerializer

