from django.urls import path
from AppEntrega import views
from django.contrib.auth.views import LogoutView


  
urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("mi_cuenta", views.mi_cuenta, name="Mi_cuenta"),
    path("libros", views.libros, name="Libros"),
    path("sucursales", views.sucursales, name="Sucursales"),
    path("contacto", views.contacto, name="Contacto"),
    path("crear_cuenta", views.crear_cuenta, name="Crear_cuenta"),
    path("busqueda", views.buscarLibro, name="buscarLibro"),
    path("buscar/", views.buscar, name="buscar"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    #path('logout', LogoutView.as_view(template_name='AppEntrega/login.html'), name='Logout'),
    path('logout',views.custom_logout, name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path("agregarAvatar", views.agregarAvatar, name="AgregarAvatar"),



]
