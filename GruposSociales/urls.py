from django.urls import path
from GruposSociales.views import amigos
from GruposSociales.views import compañeros
from GruposSociales.views import familiares

urlpatterns = [
    path('', amigos),
    path('', compañeros),
    path('', familiares),
]