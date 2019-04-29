
from ExtractPdfWeb.orc.LectorTextoEnImagenes import main
import glob
from ExtractPdfWeb.orc.Conf.Config import configuracion, test_mode





def test_all():
    """
    pruebas de integracion para modulo ExtractPDF
    Se procesran 1 a 1 todos los pdf almacenados en la carpeta input
    y ser iran probando todas las escalas de grises disponibles
    :return: str con el texto optenido apartir de orc
    """

    escalas_grises = ['B', 'T', 'BT', 'Default']


    for pdf in glob.glob('../input/*.pdf'):
        print('[+] El archivo habierto es -> ' + pdf.split('/')[2])

        for escala_gris in escalas_grises:
            print('[+] La escala de grises usada es -> ' + escala_gris)

            main(pdf.split('/')[2], escala_gris)


if __name__ == '__main__':
    configuracion['acceso_rama'] = test_mode
    test_all()