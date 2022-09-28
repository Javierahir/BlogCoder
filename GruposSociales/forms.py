from django import forms


class FormularioAmigos(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
