from datetime import date

from rest_framework import generics, viewsets
from rest_framework.decorators import permission_classes, detail_route
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .permissions import IsAuthenticatedOrPost
from .serializers import ArchivoSerializer, IpsFileSerializers
from .models import File, IpsFiles
from .tasks import orc
from .utils import fileIpCreate, servicioTraza, fileCreate, restarPeticion


@permission_classes([IsAuthenticatedOrPost])
#@detail_route(methods=['post'])
class FileView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = ArchivoSerializer

    def upload(self, request, *args, **kwargs):

        salida = dict()
        nombre: str = None
        proceso: str = None

        try:
            if not request.data.get('id'):
                print('[-][-][-] No lleva id ')

                file_serializer = ArchivoSerializer(data=request.data)
                if file_serializer.is_valid():
                    f = file_serializer.save()

                    fileIpCreate(request, f)

                    proceso = file_serializer.data.get('proceso')
                    nombre = file_serializer.data.get('documento').__str__()


                    nombre = nombre.split('/')[-1]

                    # TODO leer proceso de los datos de entrada y configurar orc

            else:
                print('[+][+][+] Lleva id ')

                proceso = self.request.data.get('proceso')
                nombre = self.request.data.get('documento')

            text = orc.delay(nombre, proceso)

            text = text.get()

            salida['ok'] = True
            salida['salida'] = text
            if request.data.get('usuario'):
                restarPeticion(request)

            servicioTraza(request, salida, FileView.__name__)
        except Exception as e:
            print(e.__repr__())
            salida['ok'] = False
            salida['error'] = e.__repr__()

        return Response(salida, status=status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated])
class RequestForMonth(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.filter(fecha_conexion__year=date.today().year, fecha_conexion__month=date.today().month)


@permission_classes([IsAuthenticated])
class RequestForDay(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.filter(fecha_conexion=date.today())


@permission_classes([IsAuthenticated])
class RequestForYear(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.filter(fecha_conexion__year=date.today().year)




@permission_classes([AllowAny])
class CoordenadasWithRequest(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.all()

    def get(self, request, *args, **kwargs):
        salida = {}
        salida['salida'] = list()
        for ip in IpsFiles.objects.all():
            salida['salida'].append({'usuario': ip.usuario.__str__(), 'lat': ip.lat, 'lon': ip.lon})
        if len(salida['salida']) > 0:
            salida['ok'] = True
        else:
            salida['ok'] = False



        servicioTraza(request, salida, CoordenadasWithRequest.__name__)

        return Response(salida, status=status.HTTP_200_OK)





