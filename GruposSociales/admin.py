from re import A
from django.contrib import admin
from GruposSociales.models import Familiares,Amigos,Compañeros
# Register your models here.
admin.site.register(Familiares)
admin.site.register(Compañeros)
admin.site.register(Amigos)