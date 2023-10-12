from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericRelation('comment')

# Crea los modelos.


class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    comments = GenericRelation(Comment)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Manga(models.Model):
    titulo = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    comments = GenericRelation(Comment)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Figura(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    comments = GenericRelation(Comment)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Juego(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    comments = GenericRelation(Comment)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
