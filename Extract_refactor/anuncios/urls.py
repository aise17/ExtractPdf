
from django.urls import path

from .views import AnuncioInferiorView, AnuncioLateralView, AnuncioSuperiroView

urlpatterns = [

    path('anunciosuperior/', AnuncioSuperiroView.as_view(), name='anuncio_superior'),
    path('anunciolateral/', AnuncioLateralView.as_view(), name='anuncio_lateral'),
    path('anunioinferior/', AnuncioInferiorView.as_view(), name='anunio_inferior'),

]