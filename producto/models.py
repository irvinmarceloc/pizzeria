from django.db import models

#Modelo de piza
class Pizzas(models.Model):
    nombre=models.CharField(max_length=30)
    precio=models.IntegerField()
    activo=models.BooleanField()

#Modelo Ingrediente
class Ingredientes(models.Model):
    nombre=models.CharField(max_length=30)
    categoria=models.BooleanField()


