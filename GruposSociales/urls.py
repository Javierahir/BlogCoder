from django.urls import path
from GruposSociales.views import inicio,amigos,compañeros,familiares,amigosform, familiaresform, compañerosform



urlpatterns = [
    path('',inicio),
    path('amigos/',amigos,name="Amigos"),
    path('familiares/',familiares,name="Familiares"),
    path('compañeros/',compañeros,name="Compañeros"),
    path('formulario',amigosform,name="Formulario de Amigos"),
    path('formulario',familiaresform,name="Formulario de Familiares"),
    path('formulario',compañerosform,name="Formulario de Amigos"),


    ]