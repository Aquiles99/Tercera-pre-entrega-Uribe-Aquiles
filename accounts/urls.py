from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    # path('logout', LogoutView.as_view(template_name='AppEntrega/login.html'), name='Logout'),
    path('logout', views.custom_logout, name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path("agregarAvatar", views.agregarAvatar, name="AgregarAvatar"),
    # path('eliminarCliente/<cliente_nombre>/', views.eliminarCliente, name="EliminarCliente"),



]
