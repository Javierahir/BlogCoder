from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView 
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from Accounts.forms import UserRegisterForm,UserUpdateForm
# Create your views here.
#views perfil
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('Perfil')
    template_name = 'Accounts/form_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user


def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "CoderBlog/inicio.html", {"mensaje": "Usuario Creado :)"})
        else:
            mensaje = 'Cometiste un error en el registro'
    formulario = UserRegisterForm()  # Formulario vacio para construir el html
    context = {
        'form': formulario,
        'mensaje': mensaje
    }

    return render(request, "Accounts/register.html", context=context)

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
                return render(request, "CoderBlog/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"Accounts/login.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"Accounts/login.html", {"mensaje":"Error, datos erroneos"})

    formulario = AuthenticationForm()
    return render(request,"Accounts/login.html", {'form':formulario} )


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('Login')

@login_required
def perfil(request):
    return render(request,'Accounts/perfil.html' )