from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from django.utils import timezone
from oauth2_provider.models import Application

import  sys


sys.path.append("../..")
#from Extract_refactor.ocr_api.models import Explicacion
#from Extract_refactor.ocr_api.serializers import ExplicaionSerializer


from anuncios.models import QuienSomos
from ocr_api.models import MinSizeDocumento
from anuncios.models import Explicacion, Bono


class Command(BaseCommand):
    help = 'Crea superadministrador'

    def handle(self, *args, **options):
        self.crearSuperuser()
        self.crearExplicacion1Inicial()
        self.crearExplicacion2Inicial()
        self.crearExplicacion3Inicial()
        self.crearApilicationOauth()
        self.crearBonoSmallCard()
        self.crearBonoMediumCard()
        self.crearBonoGrantCard()
        self.crearMinSizeDocumentoDefault()
        self.crearQuienSomos()

    def crearSuperuser(self):
        if (User.objects.filter(username='admin')):
            print('[+] El usuario superadministrador ya existe')

        else:

            user = User()
            user.username = 'admin'
            user.set_password('admin')
            user.is_superuser = True
            user.is_staff = True

            user.save()

            print('[+] superadministrador creado')


    def crearExplicacion1Inicial(self):
        if (Explicacion.objects.filter(titulo='Convertir PDF a Word')):
            print('[+] Primera explicacion ya existe')

        else:
            explicacion = Explicacion()
            explicacion.titulo = 'Utilice el software OCR'
            explicacion.contenido = 'sin instalación en su computadora. Reconocer texto y caracteres de documentos escaneados en PDF (incluidos archivos de varias páginas), fotografías e imágenes captadas por cámaras digitales.'
            explicacion.fecha_publicacion = timezone.now()
            explicacion.fecha_creacion = timezone.now()
            explicacion.publicado = True
            explicacion.titulo_imagen = 'imagen1'
            explicacion.imagen = 'http://innovagroupbcn.com/wp-content/uploads/2017/02/ocr.jpg'

            try:

                explicacion.save()

                print('[+] Primera explicacion creada')
            except:
                print('[+][+] Primera Explicacion no es valida')
                print('[+][+] Error producido -> ' + explicacion.contenido.__repr__())

    def crearExplicacion2Inicial(self):
        if (Explicacion.objects.filter(titulo='Convertir PDF a Word')):
            print('[+] Primera explicacion ya existe')

        else:
            explicacion = Explicacion()
            explicacion.titulo = 'Convertir PDF a Word'
            explicacion.contenido = 'Convierta texto e imágenes de su documento PDF escaneado al formato DOC editable. Los documentos convertidos se ven exactamente como el original: tablas, columnas y gráficos.'
            explicacion.fecha_publicacion = timezone.now()
            explicacion.fecha_creacion = timezone.now()
            explicacion.publicado = True
            explicacion.titulo_imagen = 'imagen2'
            explicacion.imagen = 'https://sitejerk.com/images/convertir-png-en-pdf-11.png'

            try:

                explicacion.save()

                print('[+] Segunda explicacion creada')
            except:
                print('[+][+] Segunda Explicacion no es valida')
                print('[+][+] Error producido -> ' + explicacion.contenido.__repr__())



    def crearExplicacion3Inicial(self):
        if (Explicacion.objects.filter(titulo='Servicio gratuito')):
            print('[+] Tercera explicacion ya existe')

        else:
            explicacion = Explicacion()
            explicacion.titulo = 'Servicio gratuito'
            explicacion.contenido = 'OnlineOCR.net es un servicio de OCR gratuito en un "modo de invitado" (sin registro) que le permite convertir 15 archivos por hora (y 15 páginas en archivos de varias páginas). El registro le dará la capacidad de convertir documentos PDF de varias páginas y otras características.'
            explicacion.fecha_publicacion = timezone.now()
            explicacion.publicado = True
            explicacion.titulo_imagen = 'imagen3'
            explicacion.imagen = 'https://st.depositphotos.com/1031343/3971/v/950/depositphotos_39717745-stock-illustration-gratis-stamp.jpg'

            try:

                explicacion.save()

                print('[+] Tercera explicacion creada')
            except:
                print('[+][+] Tercera Explicacion no es valida')
                print('[+][+] Error producido -> ' + explicacion.contenido.__repr__())



    def crearApilicationOauth(self):
        if (Application.objects.filter(client_id='xIlTUtu3pv3YCN0NZxioinzAIvnqhaUPB3j6C9m1')):
            print('[+] Tercera explicacion ya existe')
        else:
            aplication = Application()
            aplication.client_id = 'xIlTUtu3pv3YCN0NZxioinzAIvnqhaUPB3j6C9m1'
            aplication.client_secret = '15VmSMITKwQTOdDxSfUtFa6SGhvSkhRbtumDSJssPaOvhL1BJAoql5SCM6EVGdEPEubougfrpR3f29GoPDhgeez3o9kWlSQFRsd03wiJiHz9Wlgp9V61y8tdom0XyZoj'
            aplication.client_type = 'confidential'
            aplication.redirect_uris = ''
            aplication.authorization_grant_type = 'password'

            try:

                aplication.save()

                print('[+] Registro de Aplicacion creado')
            except:
                print('[+][+] Registro de Aplicacion no es valida')
                print('[+][+] Error en registro de Aplicacion -> ' + aplication.__repr__())

    def crearBonoGrantCard(self):
        if Bono.objects.filter(titulo='Great Card'):
            print('[+] Bono Great Card ya existe')
        else:
            bono = Bono()
            bono.titulo = 'Great Card'
            bono.peticiones = '200'
            bono.descripcion = 'consige el este pak de 200 peticiones a nuestro servicios a un coste reducido'
            bono.precio = '10'
            bono.activado = True

            try:
                bono.save()
                print('[+] Registro de Bono Great Card creado')
            except:

                print('[+][+] Registro de Bono no es valido')
                print('[+][+] Error en registro de Aplicacion -> ' + bono.__repr__())

    def crearBonoMediumCard(self):
        if Bono.objects.filter(titulo='Medium Card'):
            print('[+] Bono Medium Card ya existe')
        else:
            bono = Bono()
            bono.titulo = 'Medium Card'
            bono.peticiones = '80'
            bono.descripcion = 'amplia tus peticiones con este pak de 80 peticiones por solo 8 euros'
            bono.precio = '8'
            bono.activado = True

            try:
                bono.save()
                print('[+] Registro de Bono Great Card creado')
            except:

                print('[+][+] Registro de Bono no es valida')
                print('[+][+] Error en registro de Aplicacion -> ' + bono.__repr__())

    def crearBonoSmallCard(self):
        if Bono.objects.filter(titulo='Small Card'):
            print('[+] Bono Small Card ya existe')
        else:
            bono = Bono()
            bono.titulo = 'Small Card'
            bono.peticiones = '20'
            bono.descripcion = 'este bono te permitirá adquirir 20 peticiones a nuestros servicios'
            bono.precio = '5'
            bono.activado = True

            try:
                bono.save()
                print('[+] Registro de Bono Great Card creado')
            except:

                print('[+][+] Registro de Bono no es valida')
                print('[+][+] Error en registro de Aplicacion -> ' + bono.__repr__())

    def crearMinSizeDocumentoDefault(self):
        if MinSizeDocumento.objects.filter(titulo='defecto'):
            print('[+] MinSizeDocumento defecto ya existe')
        else:
            min_size_documento = MinSizeDocumento()
            min_size_documento.titulo = 'defecto'
            min_size_documento.tam_min = 40000
            min_size_documento.activo = True

            try:
                min_size_documento.save()
                print('[+] Registro de MinSizeDocumento defecto creado')
            except:

                print('[+][+] Registro de MinSizeDocumento no es valida')
                print(
                    '[+][+] Error en registro de MinSizeDocumento defecto -> ' + min_size_documento.__repr__())


    def crearQuienSomos(self):
        if QuienSomos.objects.filter(titulo='defecto'):
            print('[+] QuienSomos defecto ya existe')
        else:
            quien_somos = QuienSomos()
            quien_somos.titulo = 'defecto'
            quien_somos.contenido = '<p>Joven estudiante de programador interesado en tecnologias bakend y frontend con buen manejo en leguajes python, javascript y c# utilizando&nbsp; frameworks como django, .net, angular 5 y sql</p><p>Especializado en tecnologias python y Django utilizando el stak django, celery redis, nginx sonbre docker</p>  <p>aficionado a la escalada, los viajes las buenas conversaciones</p><p>&nbsp;</p>'
            quien_somos.publicado = True

            try:
                quien_somos.save()
                print('[+] Registro de QuienSomos defecto creado')
            except:

                print('[+][+] Registro de QuienSomos no es valida')
                print(
                    '[+][+] Error en registro de QuienSomos defecto -> ' + quien_somos.__repr__())

