import django_filters
from django import forms
from django.db.models import Q

from .models import Consola


class ConsolaFilter(django_filters.FilterSet):
    """Filtros del catálogo de consolas usando el ORM (Q, iexact, exclusiones)."""

    buscar = django_filters.CharFilter(
        method='filtrar_texto',
        label='Buscar consola',
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombre, color o descripción...'}
        ),
    )
    estado = django_filters.ChoiceFilter(
        field_name='estado',
        lookup_expr='iexact',
        label='Estado del producto',
        empty_label='Todos los estados',
        choices=(),
    )
    color = django_filters.ChoiceFilter(
        field_name='color',
        lookup_expr='iexact',
        label='Color',
        empty_label='Todos los colores',
        choices=(),
    )
    disponible = django_filters.BooleanFilter(
        method='filtrar_disponible',
        label='Solo con stock',
        widget=forms.CheckboxInput,
    )

    class Meta:
        model = Consola
        fields = ['buscar', 'estado', 'color', 'disponible']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Solo mostramos opciones de consolas que están a la venta
        vendibles = Consola.objects.filter(precio__gt=0)

        estados = (
            vendibles.values_list('estado', flat=True)
            .exclude(estado__isnull=True)
            .exclude(estado='')
            .distinct()
            .order_by('estado')
        )
        self.filters['estado'].extra['choices'] = [(e, e) for e in estados]

        colores = (
            vendibles.values_list('color', flat=True)
            .exclude(color__isnull=True)
            .exclude(color='')
            .distinct()
            .order_by('color')
        )
        self.filters['color'].extra['choices'] = [(c, c) for c in colores]

        # Estilos Bootstrap para el formulario generado por django-filter
        for field in self.form.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    def filtrar_texto(self, queryset, name, value):
        """Búsqueda con Q objects: nombre, descripción, color o identificador."""
        return queryset.filter(
            Q(nombre__icontains=value)
            | Q(descripcion__icontains=value)
            | Q(color__icontains=value)
            | Q(hardware_id__icontains=value)
        )

    def filtrar_disponible(self, queryset, name, value):
        """Exclusión: deja solo las consolas con stock mayor a cero."""
        if value:
            return queryset.exclude(stock=0)
        return queryset
