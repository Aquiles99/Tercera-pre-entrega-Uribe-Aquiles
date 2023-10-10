from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from AppEntrega.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

#MI BLOG PERSONAL
def mi_vista(request):
    return render(request, 'mi_template.html')

# Crear tus vistas aquí.

#@login_required
def inicio(request):
    return render(request, "AppEntrega/index.html")






#LIBROS
def buscarLibro(request):
      
      return render(request, "AppEntrega/buscarLibro.html")

def buscar(request):
      if request.GET["titulo"]:

            titulo= request.GET['titulo']
            mis_libros = Libro.objects.filter(titulo__icontains=titulo)

            if len(mis_libros) != 0:
             return render(request, "AppEntrega/buscarLibro.html",{"titulo":titulo, "mis_libros":mis_libros} )
            else:
                  return render(request,"AppEntrega/buscarLibro.html", {"mensaje":f"no se encontro: {titulo}"})

            #return render(request,"AppEntrega/buscarLibro.html",{"titulo":titulo, "mis_libros":mis_libros})
      
      else:

            respuesta="No se encontro ese titulo"

      return HttpResponse(respuesta)



#Creamos formularios para nuestras class.


# def libros(request):
#       mis_libros= Libro.objects.all()
 
#       if request.method == "POST":
 
#             miFormulario = LibrosFormulario(request.POST) # Aqui me llega la informacion del html
#             print(miFormulario)
 
#             if miFormulario.is_valid:
#                   informacion = miFormulario.cleaned_data
#                   curso = Libro(titulo=informacion["titulo"], genero=informacion["genero"], autor=informacion["autor"])
#                   curso.save()
#                   return redirect("Libros")
#       else:
#             miFormulario = LibrosFormulario()
 
#       return render(request, "AppEntrega/libros.html",{"miFormulario":miFormulario, "libros":mis_libros})


#lista basada en clases (CRUD)
#CRUD de libro
class ListaLibros(LoginRequiredMixin, ListView):
    model= Libro
    template_name= "AppEntrega/listaLibros.html"
    context_object_name= 'libros'

class CrearLibros(LoginRequiredMixin, CreateView):
    model= Libro
    form_class= LibroForm
    template_name= "AppEntrega/libros.html"
    success_url = reverse_lazy("Libros_lista")

class LibroDetailView(DetailView):
      model = Libro
      template_name = "AppEntrega/detalleLibro.html"  # Ruta a la plantilla de detalles
      context_object_name = 'libro'  # Nombre del objeto en el contexto

class ActualizarLibros(LoginRequiredMixin, UpdateView):
      model= Libro
      form_class= LibroForm
      template_name= "AppEntrega/libros.html"
      success_url = reverse_lazy("Libros_lista")

class BorrarLibros(LoginRequiredMixin, DeleteView):
    model= Libro
    template_name = 'AppEntrega/borrar_Libro.html'
    success_url = reverse_lazy('Libros_lista')

#CRUD manga
class ListaManga(LoginRequiredMixin, ListView):
     model= Manga
     template_name= "AppEntrega/listaManga.html"
     context_object_name= 'mangas'

class CrearMangas(LoginRequiredMixin, CreateView):
       model= Manga
       form_class= MangaForm
       template_name= "AppEntrega/manga.html"
       success_url = reverse_lazy("Manga_lista")


class MangaDetailView(DetailView):
       model = Manga
       template_name = "AppEntrega/detalleManga.html"  # Ruta a la plantilla de detalles
       context_object_name = 'manga'  # Nombre del objeto en el contexto

class ActualizarMangas(LoginRequiredMixin, UpdateView):
       model= Manga
       form_class= MangaForm
       template_name= "AppEntrega/manga.html"
       success_url = reverse_lazy("Manga_lista")

class BorrarMangas(LoginRequiredMixin, DeleteView):
     model= Manga
     template_name = 'AppEntrega/borrar_Manga.html'
     success_url = reverse_lazy('Manga_lista')    

#CRUD figuras
class ListaFigura(LoginRequiredMixin, ListView):
     model= Figura
     template_name= "AppEntrega/listaFigura.html"
     context_object_name= 'figuras'

class CrearFiguras(LoginRequiredMixin, CreateView):
       model= Figura
       form_class= FiguraForm
       template_name= "AppEntrega/figura.html"
       success_url = reverse_lazy("Figura_lista")


class FiguraDetailView(DetailView):
       model = Figura
       template_name = "AppEntrega/detalleFigura.html"  # Ruta a la plantilla de detalles
       context_object_name = 'figura'  # Nombre del objeto en el contexto

class ActualizarFiguras(LoginRequiredMixin, UpdateView):
       model= Figura
       form_class= FiguraForm
       template_name= "AppEntrega/figura.html"
       success_url = reverse_lazy("Figura_lista")

class BorrarFiguras(LoginRequiredMixin, DeleteView):
     model= Figura
     template_name = 'AppEntrega/borrar_Figura.html'
     success_url = reverse_lazy('Figura_lista')    

#CRUD juegos de mesa
class ListaJuego(LoginRequiredMixin, ListView):
     model= Juego
     template_name= "AppEntrega/listajuegos.html"
     context_object_name= 'juegos'

class CrearJuegos(LoginRequiredMixin, CreateView):
       model= Juego
       form_class= JuegosForm
       template_name= "AppEntrega/juegos.html"
       success_url = reverse_lazy("Juego_lista")


class JuegoDetailView(DetailView):
       model = Juego
       template_name = "AppEntrega/detalleJuegos.html"  # Ruta a la plantilla de detalles
       context_object_name = 'juego'  # Nombre del objeto en el contexto

class ActualizarJuegos(LoginRequiredMixin, UpdateView):
       model= Juego
       form_class= JuegosForm
       template_name= "AppEntrega/juegos.html"
       success_url = reverse_lazy("Juego_lista")

class BorrarJuegos(LoginRequiredMixin, DeleteView):
     model= Juego
     template_name = 'AppEntrega/borrar_Juegos.html'
     success_url = reverse_lazy('Juego_lista')    
