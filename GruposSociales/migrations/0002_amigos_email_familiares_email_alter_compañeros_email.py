# Generated by Django 4.1 on 2022-09-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GruposSociales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigos',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
