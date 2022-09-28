from django.shortcuts import render
from GruposSociales.models import Amigos
from GruposSociales.forms import FormularioAmigos


def inicio(request):
    return render(request, "GruposSociales/inicio.html")
def amigos(request):
   amigos= Amigos.objects.all()
   return render(request, "GruposSociales/amigos.html",{"amigos":amigos})
def compañeros(request):
   return render(request, "GruposSociales/compañeros.html")
def AboutBlog(request):
   return render(request, "GruposSociales/AboutBlog.html",{"AboutBlog":AboutBlog})
def formulario_amigos(request):

   if request.method == "POST":

      miFormulario = FormularioAmigos(request.POST)


      if miFormulario.is_valid(): 

         informacion = miFormulario.cleaned_data

         amigo = Amigos (nombre=informacion['nombre'], apellido=informacion['apellido'],edad=informacion['edad'],email=informacion['email'])

         amigo.save()

         return render(request, "GruposSociales/inicio.html") 

   else:

      miFormulario= FormularioAmigos() 

   return render(request, "GruposSociales/amigosform.html", {"miFormulario": miFormulario})
def busqueda_amigos(request):
   return render(request,"GruposSociales/busqueda_amigosform.html")
def buscar_amigos(request):
   if request.GET["nombre"]:
      nombre = request.GET["nombre"]
      amigos = Amigos.objects.filter(nombre__icontains=nombre)
      return render(request, "GruposSociales/amigos.html",{'amigos':amigos})
   else:
       return render(request, "GruposSociales/amigos.html",{'amigos':[]})
