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

from CoderBlog.models import Blog
from CoderBlog.forms import UserRegisterForm,UserUpdateForm, AvatarFormulario, FormularioBlog



#Views inicio
def inicio(request):
    return render(request, "CoderBlog/inicio.html")


def pages(request):
   return render(request, "CoderBlog/pages.html")


def AboutUs(request):
   return render(request, "CoderBlog/about.html",{"AboutUs":AboutUs})


# Views de blogs, creación, editado y borrado

def blog(request):
    blog = Blog.objects.all()
    contexto = {"blog": blog}
    borrado = request.GET.get('borrado', None)
    contexto['borrado'] = borrado

    return render(request, "CoderBlog/blog.html", contexto)


@login_required
def eliminar_blog(request,id):
    blog = Blog.objects.get(id=id)
    borrado_id = blog.id
    blog.delete()
    url_final = f"{reverse('blog')}?borrado={borrado_id}"

    return redirect(url_final)


@login_required
def crear_blog(request):
    if request.method == 'POST':
        formulario = FormularioBlog(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            blog = Blog(**data)
            # blog = Blog(apellido=data['apellido'], nombre=data['nombre'])
            blog.save()
            return redirect(reverse('blog'))
    else:  # GET
        formulario = FormularioBlog()  # Formulario vacio para construir el html
    return render(request, "CoderBlog/blog.html", {"formulario": formulario})


@login_required
def editar_blog(request, id):
    # Recibe param blog id, con el que obtenemos el blog
    blog = Blog.objects.get(id=id)

    if request.method == 'POST':
        formulario = FormularioBlog(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            blog.titulo = data['titulo']
            blog.subtitulo = data['subtitulo']
            blog.cuerpo = data['cuerpo']
            #blog.imagen = data['imagen']

            blog.save()

            return redirect(reverse('blog'))
    else:  # GET
        inicial = {
            'titulo': blog.titulo,
            'subtitulo': blog.subtitulo,
            'cuerpo': blog.cuerpo,
            #'imagen': blog.imagen,
        }
        formulario = FormularioBlog(initial=inicial)
    return render(request, "CoderBlog/blog.html", {"formulario": formulario})


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





