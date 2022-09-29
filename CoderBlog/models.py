from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"

class Blog(models.Model):
    titulo = models.CharField(max_lenght=64)
    subtitulo = models.CharField(max_lenght=64)
    cuerpo = models.CharField()
    autor = models.CharField(max_lenght=120)
    fecha = models.DateField()
    imagen = models.ImageField()

