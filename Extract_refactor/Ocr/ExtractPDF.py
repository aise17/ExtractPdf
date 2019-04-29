import glob
# de aki cojeremos la calse Image de PIL que es necesaria para pasarsela a tresseract
from PIL import Image
# con treseract extaeremos eltexto de la imagen png pasada por escala de grises
import pytesseract
# se usea OpenCv para aplicar escala de grises sobre imagen
import cv2

# usamos sistema para crear una imagen/archivo temporal y eliminarla por su PID
import os
# la uso para convertir de pdf a imagen
from wand.image import Image as Img
from Extract_refactor.settings import IMAGENES_PATH



# cargamos un pdf y obtenemos una imagen png por cada hoja del pdf

with Img(filename='Extract_refator/media' +'/factura1.pdf', resolution=300) as img:
    img.compression_quality = 50
    img.save(filename='output/image_name.jpg')




# obtenemos el numero de archivos png de la carpeta output que se an creado del pdf
number_of_images = len(glob.glob("output/*.jpg"))

print(" [+] CONTADOR ->  "+ number_of_images.__str__())



# contamos para aplicar sobre ruta de carga de imagenes creadas y mantener control del bucle
count = 0

# creamos bucle para iterar por todas la imagenes desde contador a 0 hasta number_of_images
while(count < number_of_images):

    print(" [*] PROCESANDO PAGINA NUMERO ->  " + count.__str__())

    # AQUI FALLA ALGO¡¡¡¡


    image = cv2.imread('output/image_name-'+count.__str__()+'.jpg')

    # se configura escala de grises a usar en el procesamiento de la imagen por defecto
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # estos if permiten configurar mas la escala de grisies con la que se va a proccesar la imagen con openCV
    # existen 2 maneras mas thresh o blur
    if '' == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


    elif 'blur' == "blur":
        gray = cv2.medianBlur(gray, 3)

    # escribimos la imagen procesada(en escala de grises) en el disco como una imagen/fichero temporal ,
    filename = "{}.png".format(os.getpid())

    # y sobre este aplicamos openCV
    cv2.imwrite(filename, gray)

    # cargamos la imagen con la variable tipo Image de PIL/Pillow,
    # y se aplica el ORC
    text = pytesseract.image_to_string(Image.open(filename))
    # y eliminamos la imagen temporal
    os.remove(filename)

    # por ultimo se imprime el texto
    print(text)

    #y se sumauno en la cuenta
    count += 1


# fuera del bucle y para terminal el programa borramos la imagenes creadas del PDF

for imagen in glob.glob('output/*.jpg'):
    os.remove(imagen)




