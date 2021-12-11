from django.db import models

#Modelo de piza
class Pizza(models.Model):
    nombre=models.CharField(max_length=30)
    precio=models.IntegerField()
    activo=models.BooleanField()

#Modelo Ingrediente
class Ingrediente(models.Model):
    nombre=models.CharField(max_length=30)
    categoria=models.BooleanField()


