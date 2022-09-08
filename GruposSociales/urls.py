from django.urls import path
from GruposSociales import views


urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('amigos/',views.amigos,name="Amigos"),
    path('familiares/',views.familiares,name="Familiares"),
    path('compañeros/',views.compañeros,name="Compañeros"),
    path('formulario_amigos/',views.formulario_amigos,name="Formulario de Amigos"),
    path('formulario_familiares/',views.formulario_familiares,name="Formulario de Familiares"),
    path('formulario_compañeros/',views.formulario_compañeros,name="Formulario de Compañeros"),
    path('busqueda_amigo_form/',views.busqueda_amigos,name="busqueda_amigos_form"),
    path('buscar_amigo/',views.buscar_amigos,name="buscar_amigos"), 
    path('busqueda_familiar_form/',views.busqueda_familiar,name="busqueda_familiar_form"),
    path('buscar_familiar/',views.buscar_familiar,name="buscar_familiar"),
    path('busqueda_compañero_form/',views.busqueda_compañero,name="busqueda_compañero_form"),
    path('buscar_compañero/',views.buscar_compañero,name="buscar_compañero"),
]






    
    