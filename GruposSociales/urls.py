from django.urls import path
from GruposSociales import views


urlpatterns = [
    path('',views.pages,name='Pages'),
    path('AboutBlog/',views.AboutBlog,name="AboutBlog"),
    path('amigos/',views.amigos,name="Amigos"),
    path('formulario_amigos/',views.formulario_amigos,name="Formulario de Amigos"),
    path('busqueda_amigo_form/',views.busqueda_amigos,name="busqueda_amigos_form"),
    path('buscar_amigo/',views.buscar_amigos,name="buscar_amigos"),
    #url Perfil
    path('login/',views.login_request,name="Login"),
    path('register/',views.register,name="Registro"),
    path('logout/',views.CustomLogoutView.as_view(),name="Logout"),
]






    
    