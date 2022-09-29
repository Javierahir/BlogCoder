from typing import Dict

from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView 
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from GruposSociales.models import Amigos
from GruposSociales.forms import UserRegisterForm, FormularioAmigos, UserUpdateForm, AvatarFormulario



#Views pages
def pages(request):
   return render(request, "GruposSociales/pages.html")

def AboutBlog(request):
   return render(request, "GruposSociales/AboutBlog.html",{"AboutBlog":AboutBlog})


#Views con sesión iniciada
@login_required
def inicio(request):
    return render(request, "GruposSociales/inicio.html")

@login_required
def amigos(request):
   amigos= Amigos.objects.all()
   return render(request, "GruposSociales/amigos.html",{"amigos":amigos})

@login_required
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

@login_required
def busqueda_amigos(request):
   return render(request,"GruposSociales/busqueda_amigosform.html")

@login_required
def buscar_amigos(request):
   if request.GET["nombre"]:
      nombre = request.GET["nombre"]
      amigos = Amigos.objects.filter(nombre__icontains=nombre)
      return render(request, "GruposSociales/amigos.html",{'amigos':amigos})
   else:
       return render(request, "GruposSociales/amigos.html",{'amigos':[]})

@login_required
def eliminar_amigo(request,id):
   amigos = Amigos.objects.get(id=id)
   borrado_id = amigos.id
   amigos.delete()
   url_final = f"{reverse('amigos')}?borrado={borrado_id}"

   return redirect(url_final)

@login_required
def editar_amigo(request, id):
   amigos = Amigos.objects.get(id=id)

   if request.method == 'POST':
      formulario = FormularioAmigos(request.POST)

      if formulario.is_valid():
         data = formulario.cleaned_data

         amigos.nombre = data['nombre']
         amigos.apellido = data['apellido']
         amigos.edad = data['edad']
         amigos.email = data['email']

         amigos.save()

         return redirect(reverse('amigos'))
   else: 
      inicial = {
         'nombre': amigos.nombre,
         'apellido': amigos.apellido,
         'edad': amigos.edad,
         'email': amigos.email,
      }
      formulario = FormularioAmigos(initial=inicial)
   return render(request, "GruposSociales/amigosform.html", {"formulario": formulario})


#Views de usuarios, login, logout y register

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'AppCoder/form_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

@login_required
def agregar_avatar(request):
    if request.method == 'POST':

        form = AvatarFormulario(request.POST, request.FILES) 

        if form.is_valid:   
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            return redirect(reverse('inicio'))

    form = AvatarFormulario() 
    return render(request, "AppCoder/form_avatar.html", {"form":form})

def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Usuario Creado :)"})
        else:
            mensaje = 'Cometiste un error en el registro'
    formulario = UserRegisterForm()  # Formulario vacio para construir el html
    context = {
        'form': formulario,
        'mensaje': mensaje
    }

    return render(request, "AppCoder/register.html", context=context)

def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"AppCoder/inicio.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()
    return render(request,"AppCoder/login.html", {'form':form} )


class CustomLogoutView(LogoutView):
    template_name = 'AppCoder/logout.html'
    next_page = reverse_lazy('inicio')





