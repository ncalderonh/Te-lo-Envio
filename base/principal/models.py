from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    dirección = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Productor (models.Model):
    razon_social = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    rep_legal = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    dirección = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
        
    def __str__(self):
        return self.nombre