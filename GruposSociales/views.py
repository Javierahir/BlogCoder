from django.shortcuts import render,redirect,reverse
from GruposSociales.models import Amigos
from GruposSociales.forms import UserRegister
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView 
from django.urls import reverse_lazy

#Views pages
def pages(request):
   return render(request, "GruposSociales/pages.html")

#views blogs 
def Blogs(request):
   return render(request, "GruposSociales/compañeros.html")


#views about 
def AboutBlog(request):
   return render(request, "GruposSociales/AboutBlog.html",{"AboutBlog":AboutBlog})


#views perfil
def login_request(request):
   next_url = request.GET.get('next')
   if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password= password)

            if  user:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                return render(request, "GruposSociales/pages.html", {"mensaje": "Bienvenido"})
            else:

                return render(request, "GruposSociales/login.html", {"mensaje": "Contraseña o usario erroneos"})  
        else:

            return render(request, "GruposSociales/login.html", {"mensaje": "Contraseña o usario erroneos"})  

   formulario = AuthenticationForm()  
   return render(request, "GruposSociales/login.html",{'form':formulario}) 



def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "GruposSociales/pages.html", {"mensaje": "Usuario Creado"})
        else:
            mensaje = 'Hubo un error en el registro'
    formulario = UserRegister()  
    context = {
        'form': formulario,
        'mensaje': mensaje
    }
    return render(request, "GruposSociales/register.html", context=context)


class CustomLogoutView(LogoutView):
   next_page= reverse_lazy('Login') 


