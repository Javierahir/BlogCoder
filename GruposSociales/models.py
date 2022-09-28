from django.db import models

class Amigos(models.Model):
    nombre= models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    edad = models.IntegerField()
    email= models.EmailField()

