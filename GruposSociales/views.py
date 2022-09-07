from re import A
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from GruposSociales.models import Familiares, Amigos, Compañeros 
from GruposSociales.forms import FormularioAmigos


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

def formularioAmigos(request):

   if request.method == "POST":

      miFormulario = FormularioAmigos(request.POST)

      print(miFormulario)

      if miFormulario.is_valid: #Si paso la validacion de django

         informacion = miFormulario.cleaned_data

         amigos = Amigos (nombre=informacion['nombre'], apellido=informacion['apellido'],edad=informacion['edad'],)

         amigos.save()

         return render(request, "GruposSociales/inicio.html") #Vuelta al inicio

   else:

      miFormulario= FormularioAmigos() #Formulario vacio para construir html

   return render(request, "GruposSociales/amigosform.html", {"miFormulario": miFormulario})




