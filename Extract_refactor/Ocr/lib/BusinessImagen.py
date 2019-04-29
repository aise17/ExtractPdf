import glob
# de aki cojeremos la calse Image de PIL que es necesaria para pasarsela a tresseract
from PIL import Image
# con treseract extaeremos eltexto de la imagen png pasada por escala de grises
import pytesseract
# se usea OpenCv para aplicar escala de grises sobre imagen
import cv2
# usamos sistema para crear una imagen/archivo temporal y eliminarla por su PID
import os

from Ocr.Conf.Config import configuracion

from Extract_refactor.settings import MEDIA_URL , IMAGENES_PATH, JPG_PATH

class BusinessImagen():

    def configurarEscalaDeGrisesDefecto(self,image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return gray

    def configurarEscalaDeGrisesBlur(self, image):
        gray = cv2.medianBlur(self.configurarEscalaDeGrisesDefecto(image), 3)

        return gray

    def configurarEscalaDeGrisesThresh(self, image):
        gray = cv2.threshold(self.configurarEscalaDeGrisesDefecto(image), 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        return gray


    def configuracionEscalaDeColoresThresBinary(self, image):

        gray = cv2.adaptiveThreshold(self.configurarEscalaDeGrisesDefecto(image), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                    cv2.THRESH_BINARY, 11, 2)
        return gray


    def contarImagenesGeneradas(self):
        """
        cuenta el numero de archivos acabados en jpg que existen en la carpeta output
        :return: numero de imagenes
        """
        number_of_images = len(glob.glob( JPG_PATH + configuracion['rutas_de_todas_imagenes']))

        print(" [+] NUMERO DE PAGINAS ->  " + number_of_images.__str__())

        return number_of_images

    def cargaImagen (self, count):
        """
        carga las imagenes generadas aprtir del pdf
        :param count: para iterar entreimagenessi son mas de una
        :return:  debulve una imagen tipo OpenCV
        """

        if os.path.exists(JPG_PATH + 'image_name.jpg'):
            image = cv2.imread(JPG_PATH + 'image_name.jpg')
        else:
            image = cv2.imread(JPG_PATH + 'image_name-' + count.__str__() + '.jpg')

        return image

    def aplicarEcalaDeGrises(self, gray):
        """
        escribimos la imagen procesada(en escala de grises) en el disco como una imagen/fichero temporal,
        y sobre este aplicamos openCV
        :param gray:
        :return: ruta filename temporal creado
        """

        filename = "{}.jpg".format(os.getpid())

        cv2.imwrite(filename, gray)
        #cv2.imshow('output', gray)
        #cv2.waitKey(0)

        return filename

    def aplicarORC(self, filename):
        """
        cargamos la imagen con la variable tipo Image de PIL/Pillow,
        y se aplica el ORC
        :param filename: ruta de imagen temporal
        :return: str texto extraido de imagen con tresseract-orc
        """

        text = pytesseract.image_to_string(Image.open(filename))

        # y eliminamos la imagen temporal
        os.remove(filename)

        return text

    def borrarImagenesCreadas(self):

        for imagen in glob.glob(JPG_PATH +configuracion['rutas_de_todas_imagenes']):
            os.remove(imagen)

