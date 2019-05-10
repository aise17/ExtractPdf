import sys


sys.path.append('../')

from django.db import models
import uuid
from django.contrib.auth.models import User

from anuncios.models import Bono


class Incidencia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asunto = models.CharField(max_length=100)
    contenido = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateField(auto_now=True)
    resuelta = models.BooleanField(default= False)

    def __str__(self):
        return self.asunto


class BonoUsuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bono = models.ForeignKey(Bono, on_delete=models.CASCADE, null=True)
    activado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now=True)


