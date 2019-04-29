from django.db import models
import uuid
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField, CKEditorWidget

# Create your models here.
class File(models.Model):
    PROCESOS = (
        ('B', 'B'),
        ('T', 'T'),
        ('TB', 'TB'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descripcion = models.TextField(max_length=255, blank=True)
    documento = models.FileField('Uploaded pdf')
    dateTimeUp = models.DateTimeField(auto_now=True)
    proceso = models.TextField(choices=PROCESOS, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.descripcion


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


class IpsFiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    fecha_conexion = models.DateField(auto_now=True)
    ip = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_routeable = models.NullBooleanField(null=True, blank=True)

    def __str__(self):
        return self.ip


class Incidencia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asunto = models.CharField(max_length=100)
    contenido = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateField(auto_now=True)
    resuelta = models.BooleanField(default= False)

    def __str__(self):
        return self.asunto


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