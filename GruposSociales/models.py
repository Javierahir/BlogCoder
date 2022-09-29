from django.db import models
from django.contrib.auth.models import User

class Amigos(models.Model):
    nombre= models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    edad = models.IntegerField()
    email= models.EmailField()

class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"