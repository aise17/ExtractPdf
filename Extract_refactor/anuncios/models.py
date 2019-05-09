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

class Bono(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    peticiones = models.PositiveIntegerField()
    descripcion = models.TextField(max_length=255)
    precio = models.PositiveIntegerField()
    activado = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now=True)

class Explicacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255, blank=True)
    fecha_creacion = models.DateField(auto_now=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    publicado = models.BooleanField(default=False)
    contenido = RichTextField(config_name='default')
    titulo_imagen = models.CharField(max_length=255, blank=True)
    imagen = models.URLField()

    def __str__(self):
        return self.titulo

class QuienSomos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255, blank=True)
    fecha_creacion = models.DateField(auto_now=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    publicado = models.BooleanField(default=False)
    contenido = RichTextField(config_name='default')
    titulo_imagen = models.CharField(max_length=255, blank=True)
    imagen = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.titulo

