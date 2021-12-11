from django.contrib import admin
from producto.models import *

##Para que el usuario pueda administrar las tablas desde el panel
class PizzasAdmin(admin.ModelAdmin):
    list_display=("nombre", "precio", "activo") #Para ver con formatos
    search_fields=("nombre","activo") #Para filtrar por buscador

admin.site.register(Pizzas, PizzasAdmin)