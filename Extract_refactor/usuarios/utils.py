from django.contrib.auth.models import User
from django.contrib.gis.geoip2 import GeoIP2
from ipware import get_client_ip

from .models import IpsFiles, Traza


def fileIpCreate(request, file):
    client_ip, is_routable = get_client_ip(request)
    if request.data.get('usuario'):
        user = User.objects.get(id=request.data.get('usuario'))
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
    traza = Traza()
    traza.datos_in = request.data.__repr__()
    traza.datos_out = salida

    if request.data.get('id') :
        traza.usuario = User.objects.filter(id=request.data.get('id'))

    else:
        traza.usuario = None

    traza.funcion_llamada = "" + clase + ' ' + request.method
    traza.error = False

    traza.clean()

    traza.save()

    print('[-][-] Traza generada')
