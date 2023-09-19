from django.db import models

# Crea los modelos.

class Mi_cuenta(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Libros(models.Model):
    titulo= models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    autor= models.CharField(max_length=30)
    

class Sucursales(models.Model):
    nombre= models.CharField(max_length=30)
    domicilio= models.CharField(max_length=30)

class Contacto(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()
    


