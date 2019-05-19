
from .models import MinSizeDocumento
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class IsAuthenticatedOrPost(IsAuthenticated):
    def has_permission(self, request, view):


        regla =  MinSizeDocumento.objects.get(activo=True)

        if super().has_permission(request, view):
            return True

        if not regla.tam_min:
            regla.tam_min = 40000

        if len(request.data.get('documento') or ()) < regla.tam_min:
            #print('[+][+][+] el docuemto pesa -> {} '.format(request.data.get('documento').size))
            return True

        return False
        #return super().has_permission(request, view)

