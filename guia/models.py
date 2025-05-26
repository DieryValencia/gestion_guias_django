from django.db import models
from django.contrib.auth.models import User

class Tematica(models.Model):
    titulo      = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class Guia(models.Model):
    profesor      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guias')
    programa      = models.CharField(max_length=100)
    semana        = models.IntegerField()
    fecha_creacion= models.DateTimeField(auto_now_add=True)
    estado        = models.CharField(
                       max_length=20,
                       choices=[('Borrador','Borrador'),('Publicada','Publicada')],
                       default='Borrador'
                    )
    tematica      = models.ForeignKey(Tematica, on_delete=models.PROTECT)

    def __str__(self):
        return f"Guía {self.id} – {self.programa}"

class Recurso(models.Model):
    guia = models.ForeignKey(Guia, on_delete=models.CASCADE, related_name='recursos')
    tipo = models.CharField(max_length=50)
    url  = models.URLField()

    def __str__(self):
        return f"{self.tipo} para Guía {self.guia.id}"
