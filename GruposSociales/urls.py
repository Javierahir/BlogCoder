from django.urls import path
from GruposSociales import views


urlpatterns = [
    path('inicio', views.inicio, name= 'Inicio'),
    path('pages/',views.pages,name='Pages'),
    path('AboutBlog/',views.AboutBlog,name="AboutBlog"),
    path('amigos/',views.amigos,name="Amigos"),
    path('amigosform/',views.formulario_amigos,name="Formulario de Amigos"),
    path('busqueda_amigosform/',views.busqueda_amigos,name="busqueda_amigosform"),
    path('form_perfil/',views.buscar_amigos,name="Perfil"),

    #url Perfil
    path('login/',views.login_request,name="Login"),
    path('register/',views.register,name="Registro"),
    path('logout/',views.CustomLogoutView.as_view(),name="Logout"),
]






    
    