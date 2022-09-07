from django.urls import path
from GruposSociales.views import inicio,amigos,compañeros,familiares



urlpatterns = [
    path('',inicio),
    path('amigos/',amigos,name="Amigos"),
    path('familiares/',amigos,name="Familiares"),
    path('compañeros/',amigos,name="Compañeros"),
    ]