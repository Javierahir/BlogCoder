import random
import string

from django.test import TestCase
from CoderBlog.models import Blog

class BlogTestCase(TestCase):

    def test_creacion_blog(self):
        # Test: Comprueba que puedo crear el titulo, subtitulo y cuerpo de un blog con letras random y se espera que retorne que exista un blog id y que los atributos del blog_1 coinciadan con las variables de pruebas(titulo_prueba,subtitulo_prueba,cuerpo_prueba), eso se comprueba ya que se realiza un prit con cada uno de los atributos y del blog id
        lista_letras_titulo= [random.choice(string.ascii_letters + string.digits)for _ in range(20)]
        lista_letras_subtitulo= [random.choice(string.ascii_letters + string.digits)for _ in range(20)]
        lista_letras_cuerpo= [random.choice(string.ascii_letters + string.digits)for _ in range(40)]
        titulo_prueba = "".join(lista_letras_titulo)
        subtitulo_prueba = "".join(lista_letras_subtitulo)
        cuerpo_prueba = "".join(lista_letras_cuerpo)
        blog_1 = Blog.objects.create(titulo=titulo_prueba, subtitulo=subtitulo_prueba, cuerpo=cuerpo_prueba)

        self.assertIsNotNone(blog_1.id)
        print(blog_1.id)
        self.assertEqual(blog_1.titulo, titulo_prueba)
        print(blog_1.titulo)
        self.assertEqual(blog_1.subtitulo, subtitulo_prueba)
        print(blog_1.subtitulo)
        self.assertEqual(blog_1.cuerpo, cuerpo_prueba)
        print(blog_1.cuerpo)
