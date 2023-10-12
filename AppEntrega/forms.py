from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import models
from .models import *


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'genero', 'autor', 'imagen', 'precio']


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['titulo', 'genero', 'autor', 'imagen', 'precio']


class FiguraForm(forms.ModelForm):
    class Meta:
        model = Figura
        fields = ['nombre', 'marca', 'imagen', 'precio']


class JuegosForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['nombre', 'marca', 'imagen', 'precio']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
