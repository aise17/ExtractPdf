from ckeditor.fields import RichTextField
from django.db import models
import uuid

# Create your models here.

class AnuncioSuperior(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255, blank=True)
    fecha_creacion = models.DateField(auto_now=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    publicado = models.BooleanField(default=False)
    script = RichTextField(config_name='code')

    def __str__(self):
        return self.titulo


class AnuncioLateral(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255, blank=True)
    fecha_creacion = models.DateField(auto_now=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    publicado = models.BooleanField(default=False)
    script = RichTextField(config_name='code')

    def __str__(self):
        return self.titulo


class AnuncioInferior(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255, blank=True)
    fecha_creacion = models.DateField(auto_now=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    publicado = models.BooleanField(default=False)
    script = RichTextField(config_name='code')

    def __str__(self):
        return self.titulo
