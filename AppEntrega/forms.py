from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import models
from .models import *
 
class CursoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email= forms.EmailField()

class Mi_cuentaFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()


class LibrosFormulario(forms.Form):
    titulo= forms.CharField(max_length=30)
    genero= forms.CharField(max_length=30)
    autor= forms.CharField(max_length=30)
    

class SucursalesFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    domicilio= forms.CharField(max_length=30)

class ContactoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    email= forms.EmailField()

class Crear_cuentaFormulario(forms.Form):
        nombre= forms.CharField(max_length=30)
        email= forms.EmailField()

class LoginFormulario(forms.Form):
     usuario= forms.CharField(max_length= 30)
     password= forms.CharField(max_length= 30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
     
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()


class Meta:
     
    model = User
    fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

class AvatarFormulario(forms.ModelForm):

    class Meta:

     model = Avatar
     fields = ['image']

