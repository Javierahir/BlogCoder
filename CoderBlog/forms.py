from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from CoderBlog.models import Avatar

class FormularioBlog(forms.Form):
    titulo = forms.CharField(max_length=128)
    subtitulo = forms.CharField(max_length=128)
    cuerpo = forms.CharField(max_length=500)
    #autor 
    #fecha
    #imagen


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    class Meta:
        model= User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']


class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

