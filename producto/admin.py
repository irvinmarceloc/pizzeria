from django.contrib import admin
from producto.models import *

##Para que el usuario pueda administrar las tablas desde el panel

#Administrar Pizzas
class PizzaAdmin(admin.ModelAdmin):
    list_display=("nombre", "precio", "activo") #Para ver con formatos
    search_fields=("nombre","activo") #Para filtrar por buscador
#Administrar Ingredientes
class IngredienteAdmin(admin.ModelAdmin):
    list_display=("nombre", "categoria") #Para ver con formatos
    nombre=models.CharField(max_length=30)
    categoria=models.BooleanField()


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)

