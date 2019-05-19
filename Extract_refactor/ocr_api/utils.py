from django.contrib.auth.models import User
from django.contrib.gis.geoip2 import GeoIP2
from ipware import get_client_ip

import sys
sys.path.append('../')

from usuarios.models import BonoUsuario
from usuarios.serializers import BonoUsuarioSerializer
from .models import IpsFiles, Traza, File

def fileCreate(data):
    user = User.objects.get(id=data.get('usuarioId'))
    obj = File(usuario = user)
    obj.proceso = data.get('proceso')
    obj.documento = data.get('documento')
    obj.descripcion = data.get('descripcion')

    obj.save()

    return obj

def fileIpCreate(request, file):
    client_ip, is_routable = get_client_ip(request)
    data = request.data
    if request.data.get('usuario'):
        user = User.objects.get(id=data.get('usuario'))
        ip_file = IpsFiles(usuario=user)
    else:
        ip_file = IpsFiles()
    if client_ip is None:
        ip_file.ip = 0
        ip_file.file = file
        ip_file.lat = 0
        ip_file.lon = 0

    else:
        # We got the client's IP address
        if is_routable:
            ip_file.ip = client_ip
            print('-------------------------------------------------------------')
            print(GeoIP2.city(client_ip)['latitude'])
            ip_file.lat = GeoIP2.city(client_ip)['latitude']
            ip_file.lon = GeoIP2.city(client_ip)['longitude']
            ip_file.file = file
            ip_file.is_routeable = True

        else:
            ip_file.ip = client_ip
            ip_file.file = file
            ip_file.is_routeable = False
            ip_file.lat = 0
            ip_file.lon = 0

    ip_file.save()


def servicioTraza(request,salida, clase):
    data = request.data
    traza = Traza()
    traza.datos_in = data.__repr__()
    traza.datos_out = salida.__repr__()

    if request.data.get('usuario') :
        usuario = User.objects.get(id=request.data.get('usuario'))
        traza.usuario = usuario

    else:
        traza.usuario = None

    traza.funcion_llamada = "" + clase + ' ' + request.method
    traza.error = False

    traza.save()

    print('[-][-] Traza generada')

def restarPeticion(request):

    bono_usuario = BonoUsuario.objects.filter(usuario__id=request.data.get('usuario'), activado=True)
    bono = bono_usuario.get()
    peticiones_consumidas = int(bono.peticiones_consumidas)
    print('[+][+] ---------- {} '.format(peticiones_consumidas))
    peticiones_consumidas = peticiones_consumidas - 1
    print('[+][+] ---------- {} '.format(peticiones_consumidas))

    bono_usuario.update(peticiones_consumidas=peticiones_consumidas)




