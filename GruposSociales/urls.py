from django.urls import path
from GruposSociales import views


urlpatterns = [
    path('',views.pages,name='Pages'),
    path('AboutBlog/',views.AboutBlog,name="AboutBlog"),
    path('compañeros/',views.Blogs,name="Compañeros"),
    #url Perfil
    path('login/',views.login_request,name="Login"),
    path('register/',views.register,name="Registro"),
    path('logout/',views.CustomLogoutView.as_view(),name="Logout"),
]






    
    