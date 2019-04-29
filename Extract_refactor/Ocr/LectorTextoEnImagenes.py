
from Ocr.lib.BusinessImagen import BusinessImagen
from Ocr.lib.BusinessPDF import BusinessPDF
from Ocr.Conf.Config import configuracion, aplication_mode
from Ocr.lib.Logs import Logs


def main(ruta, proceso):

    businessImage = BusinessImagen()
    businessPDF = BusinessPDF()

    logs = Logs()

    text = ''

    # CONVERTIMOS PDF EN IMAGENES SEPARADAS
    businessPDF.convertirPDFenJPG(ruta)

    numero_imagenes = businessImage.contarImagenesGeneradas()

    contador = 0

    while contador < numero_imagenes:

        print(' [*] PROCESANDO PAGINA NUMERO -> ' + contador.__str__() + ' ...')

        image = businessImage.cargaImagen(contador)

        if proceso == "B":
            grey = businessImage.configurarEscalaDeGrisesBlur(image)

        elif proceso == "T":
            grey = businessImage.configurarEscalaDeGrisesThresh(image)

        elif proceso == 'TB':
            grey = businessImage.configuracionEscalaDeColoresThresBinary(image)

        else:
            grey = businessImage.configurarEscalaDeGrisesDefecto(image)

        filename = businessImage.aplicarEcalaDeGrises(grey)

        text += businessImage.aplicarORC(filename)

        contador += 1

    text = procesText(text)

    logs.insertar(text, proceso)

    print(repr(text))
    print(text)

    businessImage.borrarImagenesCreadas()
    return text


def procesText(text):
    text = text.replace('\n\n \n', '')
    return text


if __name__ == '__main__':

    configuracion['acceso_rama'] = aplication_mode

    ruta = input('\n [+] Introduzca nombre del PDF a procesar\n'
                 '-> ')

    proceso = input('\n [+] Introduzca filtro de escala de grises que dese usar\n\n'
                    'Lista:\n'
                    '- Blur -> B\n'
                    '- Thresh -> T\n'
                    '- Thresh Binary -> TB\n'
                    '\n-> ')

    main(ruta, proceso)
