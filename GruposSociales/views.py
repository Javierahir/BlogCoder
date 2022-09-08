from django.shortcuts import render
from GruposSociales.models import Familiares, Amigos, Compañeros 
from GruposSociales.forms import FormularioAmigos,FormularioCompañeros,FormularioFamiliares


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

def formulario_familiares(request):

   if request.method == "POST":

      formulario = FormularioFamiliares(request.POST)

      if formulario.is_valid():

         informacion = formulario.cleaned_data

         familiar =Familiares(nombre=informacion['nombre'], apellido=informacion['apellido'],edad=informacion['edad'],email=informacion['email'])

         familiar.save()

         return render(request, "GruposSociales/inicio.html") 

   else:

      formulario= FormularioFamiliares() 

   return render(request, "GruposSociales/familiaresform.html", {"formulario": formulario})


def formulario_compañeros(request):

   if request.method == "POST":

      formulario = FormularioCompañeros(request.POST)


      if formulario.is_valid():

         informacion = formulario.cleaned_data

         compañeros =Compañeros(nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'])

         compañeros.save()

         return render(request, "GruposSociales/inicio.html") 

   else:

      formulario= FormularioCompañeros() 

   return render(request, "GruposSociales/compañerosform.html", {"formulario": formulario})


def busqueda_amigos(request):
   return render(request,"GruposSociales/busqueda_amigosform.html")


def buscar_amigos(request):
   if request.GET["nombre"]:
      nombre = request.GET["nombre"]
      amigos = Amigos.objects.filter(nombre__icontains=nombre)
      return render(request, "GruposSociales/amigos.html",{'amigos':amigos})
   else:
       return render(request, "GruposSociales/amigos.html",{'amigos':[]})


def busqueda_familiar(request): 
   return render(request,"GruposSociales/busqueda_familiar_form.html")    


def buscar_familiar(request):
   if request.GET["nombre"]:
      nombre = request.GET["nombre"]
      familiar = Familiares.objects.filter(nombre__icontains=nombre)
      return render(request, "GruposSociales/familiares.html",{'familiares':familiar})
   else:
       return render(request, "GruposSociales/familiares.html",{'familiares':[]})


def busqueda_compañero(request):
   return render(request,"GruposSociales/busqueda_compañero_form.html")    


def buscar_compañero(request):
   if request.GET["nombre"]:
      nombre = request.GET["nombre"]
      compañero = Compañeros.objects.filter(nombre__icontains=nombre)
      return render(request, "GruposSociales/compañeros.html",{'compañeros':compañero})
   else:
      return render(request, "GruposSociales/compañeros.html",{'compañeros':[]})