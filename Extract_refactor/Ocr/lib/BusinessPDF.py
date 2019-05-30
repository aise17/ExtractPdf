import glob


import os

from wand.image import Image as Img

from Extract_refactor.settings import MEDIA_URL , IMAGENES_PATH, JPG_PATH

class BusinessPDF():

    def convertirPDFenJPG(self, ruta):
        """
        transforma un pdf en una sucesion de imagenes, una por cada hoja del pdf
        :param ruta: ruta donde se almacena el pdf
        :return: imagenes.jpg
        """
        print('*******************************************')

        with Img(filename= IMAGENES_PATH + ruta.__str__(), resolution=150) as img:
            #img.compression_quality = 99
            img.save(filename= JPG_PATH +'image_name.jpg')


if __name__ == '__main__':

    ruta = 'factura2.pdf'
    BusinessPDF().convertirPDFenJPG(ruta)
