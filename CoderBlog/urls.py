from django.urls import path
from CoderBlog import views


urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('pages/',views.pages,name='Pages'),
    path('about/',views.AboutUs,name="AboutUs"),
    # URLS de Blogs
    path('blog/',views.BlogList.as_view(),name="Blog"),
    path('crear-blog/', views.crear_blog, name="crear_blog"),
    path('editar-blog/<int:pk>/', views.BlogUpdate.as_view(), name="editar_blog"),
    path('eliminar-blog/<int:pk>/', views.BlogDelete.as_view(), name="eliminar_blog"),
    path('detalle-blog/<int:pk>/', views.BlogDetail.as_view(), name="detalle_blog"),
]






    
    