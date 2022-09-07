from django.urls import path
from GruposSociales.views import inicio,amigos,compañeros,familiares,formulario_amigos,formulario_familiares,formulario_compañeros



urlpatterns = [
    path('',inicio,name='Inicio'),
    path('amigos/',amigos,name="Amigos"),
    path('familiares/',familiares,name="Familiares"),
    path('compañeros/',compañeros,name="Compañeros"),
    path('formulario_amigos/',formulario_amigos,name="Formulario de Amigos"),
    path('formulario_familiares',formulario_familiares,name="Formulario de Familiares"),
    path('formulario_compañeros',formulario_compañeros,name="Formulario de Compañeros"),
]
    
    