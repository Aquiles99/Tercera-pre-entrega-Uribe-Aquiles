from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from AppEntrega.forms import *

# Crear tus vistas aquí.

def inicio(request):
    return render(request, "AppEntrega/index.html")


# def Crear_cuenta(request):
#     return render(request, "AppEntrega/crear_cuenta.html")

def buscarLibro(request):
      
      return render(request, "AppEntrega/buscarLibro.html")

def buscar(request):
      if request.GET["titulo"]:

            titulo= request.GET['titulo']
            mis_libros = Libros.objects.filter(titulo__icontains=titulo)

            if len(mis_libros) != 0:
             return render(request, "AppEntrega/buscarLibro.html",{"titulo":titulo, "mis_libros":mis_libros} )
            else:
                  return render(request,"AppEntrega/buscarLibro.html", {"mensaje":f"no se encontro: {titulo}"})

            #return render(request,"AppEntrega/buscarLibro.html",{"titulo":titulo, "mis_libros":mis_libros})
      
      else:

            respuesta="No se encontro ese titulo"

      return HttpResponse(respuesta)



#Creamos formularios para nuestras class.

def Formulario(request):
      return render(request, "AppCoder/cursoFormulario.html")

def mi_cuenta(request):
      mis_cuentas= Mi_cuenta.objects.all()
 
      if request.method == "POST":
 
            miFormulario = Mi_cuentaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Mi_cuenta(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
                  curso.save()
                  return redirect("Mi_cuenta")
      else:
            miFormulario = Mi_cuentaFormulario()
 
      return render(request, "AppEntrega/mi_cuenta.html", {"miFormulario": miFormulario, "mis_cuentas":mis_cuentas})

def libros(request):
      mis_libros= Libros.objects.all()
 
      if request.method == "POST":
 
            miFormulario = LibrosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Libros(titulo=informacion["titulo"], genero=informacion["genero"], autor=informacion["autor"])
                  curso.save()
                  return redirect("Libros")
      else:
            miFormulario = LibrosFormulario()
 
      return render(request, "AppEntrega/libros.html",{"miFormulario":miFormulario, "libros":mis_libros})

def contacto(request):
      mis_contactos= Contacto.objects.all()
 
      if request.method == "POST":
 
            miFormulario = ContactoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Contacto(nombre=informacion["nombre"], email=informacion["email"])
                  curso.save()
                  return redirect("Contacto")
      else:
            miFormulario = ContactoFormulario()
 
      return render(request, "AppEntrega/contacto.html", {"miFormulario": miFormulario, "contactos":mis_contactos})

def sucursales(request):

      mis_sucursales= Sucursales.objects.all()
 
      if request.method == "POST":
 
            miFormulario = SucursalesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Sucursales(nombre=informacion["nombre"], domicilio=informacion["domicilio"])
                  curso.save()
                  return redirect("Sucursales")
      else:
            miFormulario = SucursalesFormulario()
 
      return render(request, "AppEntrega/sucursales.html", {"miFormulario": miFormulario, "sucursales":mis_sucursales})



def crear_cuentaFormulario(request):
      return render(request, "AppCoder/cursoFormulario.html")

def crear_cuenta(request):
      nuevas_cuentas= Crear_cuenta.objects.all()
 
      if request.method == "POST":
 
            miFormulario = Crear_cuentaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Crear_cuenta(nombre=informacion["nombre"], email=informacion["email"])
                  curso.save()
                  return redirect("Crear_cuenta")
      else:
            miFormulario = Crear_cuentaFormulario()
 
      return render(request, "AppEntrega/crear_cuenta.html", {"miFormulario": miFormulario, "nuevas_cuentas":nuevas_cuentas})



