from typing import Dict

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
from CoderBlog.forms import FormularioBlog



#Views inicio
def inicio(request):
    return render(request, "CoderBlog/inicio.html")


def pages(request):
   return render(request, "CoderBlog/pages.html")


def AboutUs(request):
   return render(request, "CoderBlog/about.html",{"AboutUs":AboutUs})


# Views de blogs, creación, editado y borrado

class BlogList(ListView):
    model = Blog
    template_name = "CoderBlog/blog.html"


class BlogDelete(LoginRequiredMixin,DeleteView):
    model = Blog
    success_url = reverse_lazy('Blog')


class BlogCreate(LoginRequiredMixin,CreateView):
    model = Blog
    success_url = reverse_lazy('Blog')
    fields  = [  'titulo', 'subtitulo', 'cuerpo','autor']

class BlogUpdate(LoginRequiredMixin,UpdateView):
    model = Blog 
    success_url = reverse_lazy('Blog')
    fields  = [  'titulo', 'subtitulo', 'cuerpo']


class BlogDetail(DetailView):
    model = Blog
    template_name = "CoderBlog/blog_detalle.html"