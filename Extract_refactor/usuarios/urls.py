
from django.urls import path

from .views import FilesForUser, UserDetail, AuthentificacionUsuario, LogoutUser, RequestProcessOcrByUser, \
    RegisterUser, ContactoView, BonosByUserListView

from . import views

register_uesr = views.RegisterUser.as_view({
    'post': 'crear'
})


logout = views.LogoutUser.as_view({
    'post': 'logout'
})

user_detail = views.UserDetail.as_view({
    'post': 'userDetail'
})


login = views.AuthentificacionUsuario.as_view({
    'post': 'login'
})

userStadisticRequest = views.RequestProcessOcrByUser.as_view({
    'post': 'userStadisticRequest'
})

getFilesForUser = views.FilesForUser.as_view({
    'post': 'getFilesForUser'
})

sendCommunication = views.ContactoView.as_view({
    'post': 'sendCommunication'
})

shopUserBonus = views.BonosShop.as_view({

    'post': 'shopUserBonus'
})

getUserBonus = views.BonosByUserListView.as_view({

    'post': 'getUserBonus'
})

get_user_bonus_for_year = views.BonosComprodosbyYear.as_view({
    'get': 'bonosConpardosbyYear'
})

urlpatterns = [
    path('register/', register_uesr, name='register'),
    path('logout/', logout, name='logout'),
    path('user/<pk>', user_detail, name='user'),
    path('login/', login, name='login'),
    path('request_for_user/', userStadisticRequest, name='request_for_user'),
    path('list_files/', getFilesForUser, name='files_list'),
    path('contacto/', sendCommunication, name='contacto'),
    path('comprar_bono/', shopUserBonus, name='bono_usuario'),
    path('bono_comprados_by_year/', get_user_bonus_for_year, name='bono_comprados'),
    path('getUserBonus/', getUserBonus, name='bono_comprados'),

]
