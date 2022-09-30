from django.urls import path
from CoderBlog import views


urlpatterns = [
    path('',views.inicio,name='Pages'),
    path('pages/',views.pages,name='Pages'),
    path('about/',views.AboutUs,name="AboutUs"),
    # URLS de Blogs
    path('blog/',views.blog,name="Blog"),
    path('crear-blog/', views.crear_blog, name="crear_blog"),
    path('editar-blog/<int:id>/', views.editar_blog, name="editar_blog"),
    path('eliminar-blog/<int:id>/', views.eliminar_blog, name="eliminar_blog"),
    # URLS Perfil
    path('editar-usuario/',views.ProfileUpdateView.as_view(),name="editar_usuario"),
    path('agregar-avatar/', views.agregar_avatar, name="agregar_avatar"),
    # URLS Usuario y Sesión
    path('login/',views.login_request,name="Login"),
    path('register/',views.register,name="Registro"),
    path('logout/',views.CustomLogoutView.as_view(),name="Logout"),
]






    
    