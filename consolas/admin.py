from django.contrib import admin

from .models import Consola


@admin.register(Consola)
class ConsolaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'hardware_id', 'estado', 'stock', 'precio')
    list_filter = ('estado', 'color')
    search_fields = ('nombre', 'hardware_id')
    prepopulated_fields = {'hardware_id': ('nombre',)}
