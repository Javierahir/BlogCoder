from django.urls import path
from GruposSociales.views import inicio,amigos,compañeros,familiares,formularioAmigos,formulario_familiares



urlpatterns = [
    path('',inicio),
    path('amigos/',amigos,name="Amigos"),
    path('familiares/',familiares,name="Familiares"),
    path('compañeros/',compañeros,name="Compañeros"),
    path('formulario_amigos/',formularioAmigos,name="Formulario de Amigos"),
    path('formulario',formulario_familiares,name="Formulario de Familiares"),
    ]
    
    #path('formulario',compañerosform,name="Formulario de Amigos"),