from django.urls import path
from CoderBlog import views


urlpatterns = [
    path('',views.pages,name='Pages'),
    path('AboutBlog/',views.AboutBlog,name="AboutBlog"),
    path('blogs/',views.blogs,name="Blog"),
    path('editar-usuario/',views.ProfileUpdateView.as_view(),name="editar_usuario"),
    #url Perfil
    path('login/',views.login_request,name="Login"),
    path('register/',views.register,name="Registro"),
    path('logout/',views.CustomLogoutView.as_view(),name="Logout"),
]






    
    