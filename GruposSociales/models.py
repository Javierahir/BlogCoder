from django.db import models

class Familiares(models.Model):
    nombre= models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    edad=models.IntegerField()
    email= models.EmailField()


class Amigos(models.Model):
    nombre= models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    edad = models.IntegerField()
    email= models.EmailField()


class Compañeros(models.Model):
    nombre= models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    email= models.EmailField()
