# Generated by Django 4.1 on 2022-09-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoderBlog', '0003_avatar_delete_amigos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128)),
                ('subtitulo', models.CharField(max_length=128)),
                ('cuerpo', models.CharField(max_length=500)),
            ],
        ),
    ]
