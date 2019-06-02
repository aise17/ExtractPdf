import sys


sys.path.append('../')

from django.db import models
import uuid
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


from contenido.models import Bono


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
    peticiones_restantes = models.PositiveIntegerField(default=0)


    def save(self, *args, **kwargs):
        if self.activado:
            otros = BonoUsuario.objects.filter(activado=True)
            if self.usuario:
                otros = otros.filter(usuario=self.usuario)
            otros.update(activado=False)

        super(BonoUsuario, self).save(*args, **kwargs)


class MarketingCampaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuarios = models.ManyToManyField(User)
    asunto = models.CharField(max_length=100)
    contenido = RichTextField(config_name='default')
    fecha_creacion = models.DateField(auto_now=True)
    lanzada = models.BooleanField(default=True)
    fecha_publicacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.asunto




