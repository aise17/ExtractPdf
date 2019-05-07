
from django.urls import path

from .views import FileView, ExplicacionContent, ContactoView, RequestForMonth, RequestForYear, RequestForDay,\
    CoordenadasWithRequest, QuienesSomos

urlpatterns = [
    path('upload/', FileView.as_view(), name='file-upload'),
    path('explicacion/', ExplicacionContent.as_view(), name='explicacion'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('request-day/', RequestForDay.as_view(), name='dia'),
    path('request-mes/', RequestForMonth.as_view(), name='mes'),
    path('request-ano/', RequestForYear.as_view(), name='ano'),
    path('coor/', CoordenadasWithRequest.as_view(), name='coor'),
    path('quienSomos/', QuienesSomos.as_view(), name='quienSomos'),

]