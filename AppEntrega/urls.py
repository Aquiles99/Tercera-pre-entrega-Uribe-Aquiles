from django.urls import path
from AppEntrega import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("mi_vista", views.mi_vista, name="Mi vista"),
    path("libros", views.CrearLibros.as_view(), name="Libros"),
    path("libros_lista", views.ListaLibros.as_view(), name="Libros_lista"),
    path("detalle_libro/<int:pk>/",
         views.LibroDetailView.as_view(), name="Detalle_libro"),
    path("actualizar_libro/<int:pk>/",
         views.ActualizarLibros.as_view(), name="Actualizar_libro"),
    path("eliminar_libro/<int:pk>/",
         views.BorrarLibros.as_view(), name="Eliminar_libro"),
    path("manga", views.CrearMangas.as_view(), name="Mangas"),
    path("manga_lista", views.ListaManga.as_view(), name="Manga_lista"),
    path("detalle_manga/<int:pk>/",
         views.MangaDetailView.as_view(), name="Detalle_manga"),
    path("actualizar_manga/<int:pk>/",
         views.ActualizarMangas.as_view(), name="Actualizar_manga"),
    path("eliminar_manga/<int:pk>/",
         views.BorrarMangas.as_view(), name="Eliminar_manga"),
    path("figura", views.CrearFiguras.as_view(), name="Figuras"),
    path("figura_lista", views.ListaFigura.as_view(), name="Figura_lista"),
    path("detalle_figura/<int:pk>/",
         views.FiguraDetailView.as_view(), name="Detalle_figura"),
    path("actualizar_figura/<int:pk>/",
         views.ActualizarFiguras.as_view(), name="Actualizar_figura"),
    path("eliminar_figura/<int:pk>/",
         views.BorrarFiguras.as_view(), name="Eliminar_figura"),
    path("juego", views.CrearJuegos.as_view(), name="Juegos"),
    path("juego_lista", views.ListaJuego.as_view(), name="Juego_lista"),
    path("detalle_juego/<int:pk>/",
         views.JuegoDetailView.as_view(), name="Detalle_juego"),
    path("actualizar_juego/<int:pk>/",
         views.ActualizarJuegos.as_view(), name="Actualizar_juego"),
    path("eliminar_juego/<int:pk>/",
         views.BorrarJuegos.as_view(), name="Eliminar_juego"),
    path("busqueda", views.buscarLibro, name="buscarLibro"),
    path("buscar/", views.buscar, name="buscar"),
    # Vista para crear comentarios
    path('comment/create/<int:content_type_id>/<int:object_id>/',
         views.create_comment, name='create_comment'),



]
