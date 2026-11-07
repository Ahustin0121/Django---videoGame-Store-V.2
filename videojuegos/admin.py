from django.contrib import admin

from .models import Paquete, Videojuego


@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'consola', 'consola_manual', 'precio', 'stock', 'estado')
    list_filter = ('estado', 'consola')
    search_fields = ('nombre', 'descripcion', 'consola_manual')
    list_editable = ('precio', 'stock')
    list_select_related = ('consola',)


@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'consola', 'videojuego', 'descuento', 'activo')
    list_filter = ('activo', 'consola')
    search_fields = ('nombre', 'consola__nombre', 'videojuego__nombre')
    list_select_related = ('consola', 'videojuego')
