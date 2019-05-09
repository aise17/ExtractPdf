from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Incidencia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asunto = models.CharField(max_length=100)
    contenido = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateField(auto_now=True)
    resuelta = models.BooleanField(default= False)

    def __str__(self):
        return self.asunto