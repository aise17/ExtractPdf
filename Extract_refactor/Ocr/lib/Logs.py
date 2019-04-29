
import time
from Ocr.Conf.Config import configuracion
from Extract_refactor.settings import BASE_DIR

class Logs():


    def insertar(self,texto, proceso):

        if proceso == '':
            proceso = 'default'

        log = '\n\n\n-------------------------------------\n'
        log += 'FECHA: ' + time.strftime('%c') + '  ESCALA DE GRISES: ' + proceso + '\n'
        log += '-------------------------------------\n\n\n'

        log += texto

        with open(BASE_DIR + "/salida.txt", 'a') as f:
            f.write(log)


