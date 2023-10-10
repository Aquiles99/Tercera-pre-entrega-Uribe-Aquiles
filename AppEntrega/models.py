from django.db import models
from django.contrib.auth.models import User



# Crea los modelos.
class Libro(models.Model):
    titulo= models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    autor= models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Manga(models.Model):
    titulo= models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    autor= models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Figura(models.Model):
    nombre= models.CharField(max_length=30)
    marca= models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Juego(models.Model):
    nombre= models.CharField(max_length=30)
    marca= models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

# class Producto(models.Model):
#     nombre = models.CharField(max_length=100)
#     descripcion = models.TextField()
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
#     imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

#     def __str__(self):
#         return self.nombre    





