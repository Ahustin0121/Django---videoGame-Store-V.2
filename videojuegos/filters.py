import django_filters
from django import forms
from django.db.models import Q

from consolas.models import Consola

from .models import Videojuego


class VideojuegoFilter(django_filters.FilterSet):
    """Filtros del catálogo usando el ORM de Django (lookups gte, lte, icontains, Q)."""

    buscar = django_filters.CharFilter(
        method='filtrar_texto',
        label='Buscar juego',
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombre o descripción...'}
        ),
    )
    consola = django_filters.ModelChoiceFilter(
        queryset=Consola.objects.all(),
        label='Consola compatible',
        empty_label='Todas las consolas',
    )
    estado = django_filters.ChoiceFilter(
        field_name='estado',
        lookup_expr='iexact',
        label='Estado del producto',
        empty_label='Todos los estados',
        choices=(),
    )
    precio_min = django_filters.NumberFilter(
        field_name='precio',
        lookup_expr='gte',
        label='Precio mínimo',
        widget=forms.NumberInput(
            attrs={'placeholder': 'Desde $', 'min': 0, 'step': 100}
        ),
    )
    precio_max = django_filters.NumberFilter(
        field_name='precio',
        lookup_expr='lte',
        label='Precio máximo',
        widget=forms.NumberInput(
            attrs={'placeholder': 'Hasta $', 'min': 0, 'step': 100}
        ),
    )
    disponible = django_filters.BooleanFilter(
        method='filtrar_disponible',
        label='Solo con stock',
        widget=forms.CheckboxInput,
    )

    class Meta:
        model = Videojuego
        fields = [
            'buscar',
            'consola',
            'estado',
            'precio_min',
            'precio_max',
            'disponible',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Opciones de estado tomadas dinámicamente desde la base de datos
        estados = (
            Videojuego.objects.values_list('estado', flat=True)
            .exclude(estado__isnull=True)
            .exclude(estado='')
            .distinct()
            .order_by('estado')
        )
        self.filters['estado'].extra['choices'] = [(e, e) for e in estados]

        # Estilos Bootstrap para el formulario generado por django-filter
        for field in self.form.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    def filtrar_texto(self, queryset, name, value):
        """Búsqueda con Q objects: coincide en el nombre O en la descripción."""
        return queryset.filter(
            Q(nombre__icontains=value) | Q(descripcion__icontains=value)
        )

    def filtrar_disponible(self, queryset, name, value):
        """Exclusión: deja solo los juegos con stock mayor a cero."""
        if value:
            return queryset.exclude(stock=0)
        return queryset
