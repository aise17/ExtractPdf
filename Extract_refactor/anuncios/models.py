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

    def save(self, *args, **kwargs):
        if self.publicado:
            otros = AnuncioSuperior.objects.filter(publicado=True)
            if self.id:
                otros = otros.exclude(pk=self.id)
            otros.update(publicado=False)

        super(AnuncioSuperior, self).save(*args, **kwargs)


class AnuncioLateral(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255, blank=True)
    fecha_creacion = models.DateField(auto_now=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    publicado = models.BooleanField(default=False)
    script = RichTextField(config_name='code')

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if self.publicado:
            otros = AnuncioLateral.objects.filter(publicado=True)
            if self.id:
                otros = otros.exclude(pk=self.id)
            otros.update(publicado=False)

        super(AnuncioLateral, self).save(*args, **kwargs)


class AnuncioInferior(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255, blank=True)
    fecha_creacion = models.DateField(auto_now=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    publicado = models.BooleanField(default=False)
    script = RichTextField(config_name='code')

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if self.publicado:
            otros = AnuncioInferior.objects.filter(publicado=True)
            if self.id:
                otros = otros.exclude(pk=self.id)
            otros.update(publicado=False)

        super(AnuncioInferior, self).save(*args, **kwargs)

class Bono(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255, blank=True)
    peticiones = models.PositiveIntegerField()
    descripcion = models.TextField(max_length=255)
    precio = models.PositiveIntegerField()
    activado = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo


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

    def save(self, *args, **kwargs):
        if self.publicado:
            otros = QuienSomos.objects.filter(publicado=True)
            if self.id:
                otros = otros.exclude(pk=self.id)
            otros.update(publicado=False)

        super(QuienSomos, self).save(*args, **kwargs)

