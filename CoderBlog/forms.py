from django import forms
from CoderBlog.models import Blog

class BlogFormulario(forms.ModelForm):
    class Meta:
        model= Blog
        fields = ['titulo','subtitulo','cuerpo']


