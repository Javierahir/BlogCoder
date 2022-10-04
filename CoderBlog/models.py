from time import timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from ckeditor.fields import RichTextField


class Blog (models.Model):
    titulo = models.CharField(max_length=128)
    subtitulo = models.CharField(max_length=128)
    cuerpo = RichTextField(blank=True, null=True) 
    autor = models.ForeignKey(User,on_delete=models.CASCADE,null=True) #hay que arreglarlo
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to = 'imagenes_blogs', null=True,blank=True)

    def __str__(self):
        return f'{self.titulo}'