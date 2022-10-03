from typing import Dict
from urllib import request

from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView 
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from CoderBlog.models import Blog
from CoderBlog.forms import BlogFormulario



#Views inicio
def inicio(request):
    return render(request, "CoderBlog/inicio.html")

def AboutUs(request):
   return render(request, "CoderBlog/about.html",{"AboutUs":AboutUs})


# Views de blogs, creación, editado y borrado

class BlogList(ListView):
    model = Blog
    template_name = "CoderBlog/blog.html"


class BlogDelete(LoginRequiredMixin,DeleteView):
    model = Blog
    success_url = reverse_lazy('Blog')


@login_required
def crear_blog(request):
    if request.method == 'POST':
        form = BlogFormulario(request.POST,request.FILES)

        if form.is_valid():
            blog = form.save()
            blog.autor = request.user
            blog.save()
            return redirect(reverse('Blog'))
    else:  # GET
        form = BlogFormulario()  # Formulario vacio para construir el html
    return render(request, "CoderBlog/blog_form.html", {"form": form})

class BlogUpdate(LoginRequiredMixin,UpdateView):
    model = Blog 
    success_url = reverse_lazy('Blog')
    fields  = [  'titulo', 'subtitulo', 'cuerpo']


class BlogDetail(DetailView):
    model = Blog
    template_name = "CoderBlog/blog_detalle.html"