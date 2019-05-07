
from django.urls import path

from .views import FilesForUser, UserDetail, AuthentificacionUsuario, LogoutUser, RequestProcessOcrForUser, RegisterUser

urlpatterns = [
    path('list_files/', FilesForUser.as_view(), name='files_list'),
    path('request_for_user/', RequestProcessOcrForUser.as_view(), name='request_for_user'),
    path('user/<pk>', UserDetail.as_view(), name='user'),
    path('login/', AuthentificacionUsuario.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

]