from django.urls import path
from GruposSociales import views


urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('amigos/',views.amigos,name="Amigos"),
    path('AboutBlog/',views.AboutBlog,name="AboutBlog"),
    path('compañeros/',views.compañeros,name="Compañeros"),
    path('formulario_amigos/',views.formulario_amigos,name="Formulario de Amigos"),
    path('busqueda_amigo_form/',views.busqueda_amigos,name="busqueda_amigos_form"),
    path('buscar_amigo/',views.buscar_amigos,name="buscar_amigos"), 
]






    
    