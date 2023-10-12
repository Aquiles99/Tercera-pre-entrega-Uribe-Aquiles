from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import *

# Create your views here.


def login_request(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "AppEntrega/index.html", {"mensaje": f"Bienvenido {usuario}"})

            else:
                print("uno")
                form = AuthenticationForm()
                return render(request, "accounts/login.html", {'form': form})

        else:
            print("dos")
            form = AuthenticationForm()
            return render(request, "accounts/login.html", {'form': form})

    print("NO fue un post")
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})

# crear vista de registro


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return redirect("Login")

    else:
        form = UserRegisterForm()

    return render(request, "accounts/registro.html", {"form": form})


def custom_logout(request):
    # Realiza el cierre de sesión
    logout(request)

    return redirect("Login")

# Edicion de usuario


@login_required
def editarPerfil(request):

    # login
    usuario = request.user

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, instance=request.user)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]

        # Actualiza la contraseña solo si se proporciona una nueva contraseña
            new_password = informacion.get("password1")
            if new_password:
                usuario.set_password(new_password)

            usuario.save()

            return redirect("Login")

    else:

        miFormulario = UserEditForm(instance=request.user, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })

    return render(request, "accounts/editarPerfil.html", {"miFormulario": miFormulario, "uruario": usuario})


@login_required
def agregarAvatar(request):

    if request.method == "POST":

        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            avatar_anterior = Avatar.objects.filter(user=request.user)
            if (len(avatar_anterior) > 0):
                avatar_anterior.delete()
            avatar_nuevo = Avatar(
                user=request.user, image=miFormulario.cleaned_data["image"])
            avatar_nuevo.save()

    else:
        miFormulario = AvatarFormulario()

    return render(request, "accounts/agregarAvatar.html", {"miFormulario": miFormulario})
