from django.db import models
import uuid


class MinSizeDocumento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(default='defecto', max_length=255)
    tam_min = models.PositiveIntegerField(default=40000)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if self.activo:
            otros = MinSizeDocumento.objects.filter(activo=True)
            if self.id:
                otros = otros.exclude(pk=self.id)
            otros.update(activo=False)

        super(MinSizeDocumento, self).save(*args, **kwargs)