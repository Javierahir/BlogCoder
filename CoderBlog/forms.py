from django import forms

class FormularioBlog(forms.Form):
    titulo = forms.CharField(max_length=128)
    subtitulo = forms.CharField(max_length=128)
    cuerpo = forms.CharField(max_length=500)
    #imagen





