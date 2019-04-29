
from django.urls import path

from .views import FileView, AnuncioInferiorView, AnuncioLateralView, AnuncioSuperiroView, ExplicacionContent, \
    FilesForUser, ContactoView, RequestForMonth, RequestForYear, RequestForDay, CoordenadasWithRequest, \
    UserDetail, AuthentificacionUsuario, LogoutUser, RequestProcessOcrForUser, QuienesSomos, RegisterUser

urlpatterns = [
    path('upload/', FileView.as_view(), name='file-upload'),
    path('explicacion/', ExplicacionContent.as_view(), name='explicacion'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('anunciosuperior/', AnuncioSuperiroView.as_view(), name='anuncio_superior'),
    path('anunciolateral/', AnuncioLateralView.as_view(), name='anuncio_lateral'),
    path('anunioinferior/', AnuncioInferiorView.as_view(), name='anunio_inferior'),
    path('list_files/', FilesForUser.as_view(), name='files_list'),
    path('request-day/', RequestForDay.as_view(), name='dia'),
    path('request-mes/', RequestForMonth.as_view(), name='mes'),
    path('request-ano/', RequestForYear.as_view(), name='ano'),
    path('coor/', CoordenadasWithRequest.as_view(), name='coor'),
    path('request_for_user/', RequestProcessOcrForUser.as_view(), name='request_for_user'),
    path('user/<pk>', UserDetail.as_view(), name='user'),
    path('login/', AuthentificacionUsuario.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('quienSomos/', QuienesSomos.as_view(), name='quienSomos'),

]