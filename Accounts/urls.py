
from django.urls import path
from Accounts import views


urlpatterns = [
# URLS Perfil
    path('editar-usuario/',views.ProfileUpdateView.as_view(),name="editar_usuario"),
    path('perfil/',views.perfil, name='Perfil'),
    # URLS Usuario y Sesión
    path('login/',views.login_request,name="Login"),
    path('register/',views.register,name="Registro"),
    path('logout/',views.CustomLogoutView.as_view(),name="Logout"),
]