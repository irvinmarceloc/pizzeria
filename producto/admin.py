from django.contrib import admin


##Para que el usuario pueda administrar las tablas desde el panel
class PizzasAdmin(admin.ModelAdmin):
    list_display=("nombre", "precio", "activo") #Para ver con formatos
    search_fields=("nombre","activo") #Para filtrar por buscador
