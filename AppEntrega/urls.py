from django.urls import path

from AppEntrega import views

  
urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("mi_cuenta", views.mi_cuenta, name="Mi_cuenta"),
    path("libros", views.libros, name="Libros"),
    path("sucursales", views.sucursales, name="Sucursales"),
    path("contacto", views.contacto, name="Contacto"),
    path("crear_cuenta", views.crear_cuenta, name="Crear_cuenta"),
    path("busqueda", views.buscarLibro, name="buscarLibro"),
    path("buscar/", views.buscar, name="buscar")

]
