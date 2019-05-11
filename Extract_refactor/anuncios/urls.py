
from django.urls import path

from .views import AnuncioInferiorView, AnuncioLateralView, AnuncioSuperiroView, BonosView, ExplicacionInicio, \
    QuienesSomosView

urlpatterns = [

    path('anunciosuperior/', AnuncioSuperiroView.as_view(), name='anuncio_superior'),
    path('anunciolateral/', AnuncioLateralView.as_view(), name='anuncio_lateral'),
    path('anunioinferior/', AnuncioInferiorView.as_view(), name='anunio_inferior'),
    path('bonos/', BonosView.as_view(), name='bonos'),
    path('explicacion-inicio/', ExplicacionInicio.as_view(), name='contenido_inicio'),
    path('quien-somos/', QuienesSomosView.as_view(), name='quienSomos'),

]