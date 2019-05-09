from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from django.utils import timezone
from oauth2_provider.models import Application

import  sys
sys.path.append("../..")
#from Extract_refactor.ocr_api.models import Explicacion
#from Extract_refactor.ocr_api.serializers import ExplicaionSerializer


from  anuncios.models import Explicacion
from  anuncios.serializers import ExplicaionSerializer


data = {
    'titulo': 'Utilice el software OCR',
    'contenido': 'sin instalación en su computadora. Reconocer texto y caracteres de documentos escaneados en PDF (incluidos archivos de varias páginas), fotografías e imágenes captadas por cámaras digitales.',
    'fecha_publicacion': '2019-08-08',
    'publicado': 'True',
    'titulo_imagen': 'imagen1',
    'imagen': 'https://www.google.es/imgres?imgurl=https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1200%2F1*kMUgsKRq0rhkN4JD9HrmSw.png&imgrefurl=https%3A%2F%2Fcodeburst.io%2Foptical-character-recognition-recognizing-text-to-labels-on-an-android-platform-4c20bddc9175&docid=P4SRErQIoTG6rM&tbnid=L1XM5RgQ930N3M%3A&vet=10ahUKEwiY3vCuwYviAhWM8eAKHac_Df4QMwhMKA4wDg..i&w=600&h=411&client=ubuntu&bih=912&biw=1866&q=ocr&ved=0ahUKEwiY3vCuwYviAhWM8eAKHac_Df4QMwhMKA4wDg&iact=mrc&uact=8'
}


# explicacion.imagen = 'https://www.google.es/imgres?imgurl=https%3A%2F%2Fstore-images.s-microsoft.com%2Fimage%2Fapps.4294.13510798886736958.a650f2a3-9e4d-4aeb-8aff-d1ce5d232c80.cf7f9fcd-4d78-4d3f-8a03-98ed771f89c1&imgrefurl=https%3A%2F%2Fwww.microsoft.com%2Fes-mx%2Fp%2Fphoto-to-text-ocr%2F9nblggh6hrzh&docid=GqWOzJRBLYwspM&tbnid=nOcRfHBULMXQCM%3A&vet=10ahUKEwjS9YGqvIviAhV77OAKHbkgBUAQMwhAKAIwAg..i&w=620&h=620&client=ubuntu&bih=863&biw=1866&q=ocr&ved=0ahUKEwjS9YGqvIviAhV77OAKHbkgBUAQMwhAKAIwAg&iact=mrc&uact=8'


class Command(BaseCommand):
    help = 'Crea superadministrador'

    def handle(self, *args, **options):
        self.crearSuperuser()
        self.crearExplicacion1Inicial()
        self.crearExplicacion2Inicial()
        self.crearExplicacion3Inicial()
        self.registerApilicationOauth()

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

    '''
        def crearExplicacion1Inicial(self):
            if (Explicacion.objects.filter(titulo='Utilice el software OCR')):
                print('[+] Primera explicacion ya existe')

            else:
                #explicacion.imagen = 'https://www.google.es/imgres?imgurl=https%3A%2F%2Fstore-images.s-microsoft.com%2Fimage%2Fapps.4294.13510798886736958.a650f2a3-9e4d-4aeb-8aff-d1ce5d232c80.cf7f9fcd-4d78-4d3f-8a03-98ed771f89c1&imgrefurl=https%3A%2F%2Fwww.microsoft.com%2Fes-mx%2Fp%2Fphoto-to-text-ocr%2F9nblggh6hrzh&docid=GqWOzJRBLYwspM&tbnid=nOcRfHBULMXQCM%3A&vet=10ahUKEwjS9YGqvIviAhV77OAKHbkgBUAQMwhAKAIwAg..i&w=620&h=620&client=ubuntu&bih=863&biw=1866&q=ocr&ved=0ahUKEwjS9YGqvIviAhV77OAKHbkgBUAQMwhAKAIwAg&iact=mrc&uact=8'


                ser = ExplicaionSerializer(data=data)



                if ser.is_valid():
                    ser.save();
                    print('[+] Primera explicacion creada')
                else:
                    print('[+][+] Primera Explicacion no es valida')
                    print('[+][+] Error producido -> ' + ser.errors.__repr__())
    '''

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
            # explicacion.imagen = 'https://www.google.es/imgres?imgurl=https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1200%2F1*kMUgsKRq0rhkN4JD9HrmSw.png&imgrefurl=https%3A%2F%2Fcodeburst.io%2Foptical-character-recognition-recognizing-text-to-labels-on-an-android-platform-4c20bddc9175&docid=P4SRErQIoTG6rM&tbnid=L1XM5RgQ930N3M%3A&vet=10ahUKEwiY3vCuwYviAhWM8eAKHac_Df4QMwhMKA4wDg..i&w=600&h=411&client=ubuntu&bih=912&biw=1866&q=ocr&ved=0ahUKEwiY3vCuwYviAhWM8eAKHac_Df4QMwhMKA4wDg&iact=mrc&uact=8'

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
            #explicacion.imagen = 'https://www.google.es/imgres?imgurl=https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1200%2F1*kMUgsKRq0rhkN4JD9HrmSw.png&imgrefurl=https%3A%2F%2Fcodeburst.io%2Foptical-character-recognition-recognizing-text-to-labels-on-an-android-platform-4c20bddc9175&docid=P4SRErQIoTG6rM&tbnid=L1XM5RgQ930N3M%3A&vet=10ahUKEwiY3vCuwYviAhWM8eAKHac_Df4QMwhMKA4wDg..i&w=600&h=411&client=ubuntu&bih=912&biw=1866&q=ocr&ved=0ahUKEwiY3vCuwYviAhWM8eAKHac_Df4QMwhMKA4wDg&iact=mrc&uact=8'

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
            #explicacion.imagen = 'https://www.google.es/imgres?imgurl=https%3A%2F%2Fwww.nerdwallet.com%2Fassets%2Fblog%2Fwp-content%2Fuploads%2F2014%2F11%2FiStock_000079110987_Small-570x225.jpg&imgrefurl=https%3A%2F%2Fwww.nerdwallet.com%2Fblog%2Fcredit-cards%2Fcredit-cards-give-free-fico-scores%2F&docid=bpjK7F9a2KAijM&tbnid=7hEcTu8Qo8y_gM%3A&vet=10ahUKEwjhqtnovIviAhWPHRQKHWMqBgoQMwg9KAUwBQ..i&w=570&h=225&client=ubuntu&bih=863&biw=1866&q=free&ved=0ahUKEwjhqtnovIviAhWPHRQKHWMqBgoQMwg9KAUwBQ&iact=mrc&uact=8'

            try:

                explicacion.save()

                print('[+] Tercera explicacion creada')
            except:
                print('[+][+] Tercera Explicacion no es valida')
                print('[+][+] Error producido -> ' + explicacion.contenido.__repr__())



    def registerApilicationOauth(self):
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