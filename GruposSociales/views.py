from re import A
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from GruposSociales.models import Familiares, Amigos, Compañeros 


def inicio(request):
    return render(request, "GruposSociales/inicio.html")


def amigos(request):
   amigos= Amigos.objects.all()
   return render(request, "GruposSociales/amigos.html",{"amigos":amigos})


def compañeros(request):
   compañeros= Compañeros.objects.all()
   return render(request, "GruposSociales/compañeros.html",{"compañeros":compañeros})


def familiares(request):
   familiares= Familiares.objects.all()
   return render(request, "GruposSociales/familiares.html",{"familiares":familiares})