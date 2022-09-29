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
from CoderBlog.forms import UserRegisterForm,UserUpdateForm, AvatarFormulario



#Views pages
def pages(request):
   return render(request, "CoderBlog/pages.html")


def AboutBlog(request):
   return render(request, "CoderBlog/AboutBlog.html",{"AboutBlog":AboutBlog})


def blogs(request):
    return render(request,"CoderBlog/blog.html",{"blogs":blogs})


#views perfil
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('Pages')
    template_name = 'CoderBlog/form_perfil.html'

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
            return redirect(reverse('pages'))

    form = AvatarFormulario() 
    return render(request, "CoderBlog/form_avatar.html", {"form":form})

def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "CoderBlog/pages.html", {"mensaje": "Usuario Creado :)"})
        else:
            mensaje = 'Cometiste un error en el registro'
    formulario = UserRegisterForm()  # Formulario vacio para construir el html
    context = {
        'form': formulario,
        'mensaje': mensaje
    }

    return render(request, "CoderBlog/register.html", context=context)

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
                return render(request, "CoderBlog/pages.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"CoderBlog/pages.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"CoderBlog/pages.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()
    return render(request,"CoderBlog/login.html", {'form':form} )


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('Login')





