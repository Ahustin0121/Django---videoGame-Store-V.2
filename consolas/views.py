from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .filters import ConsolaFilter
from .forms import ConsolaForm
from .models import Consola


class ConsolaListView(ListView):
    """Catálogo público: solo consolas que realmente están a la venta."""

    model = Consola
    template_name = 'consolas/consolas.html'
    context_object_name = 'productos'

    def get_queryset(self):
        # Las plataformas cargadas solo para asociar videojuegos tienen precio 0
        queryset = super().get_queryset().filter(precio__gt=0)
        # Conectamos request.GET con el FilterSet
        self.filterset = ConsolaFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pasamos el formulario de filtros al template
        context['form'] = self.filterset.form
        return context


class ConsolaDetailView(DetailView):
    model = Consola
    template_name = 'consolas/detalle.html'
    context_object_name = 'producto'
    slug_field = 'hardware_id'
    slug_url_kwarg = 'hardware_id'

    def get_queryset(self):
        # Traemos también los videojuegos asociados (relación inversa)
        return super().get_queryset().prefetch_related('videojuegos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paquetes'] = self.object.paquetes.filter(activo=True).select_related(
            'videojuego'
        )
        return context


class ConsolaManageListView(LoginRequiredMixin, ListView):
    """Panel de administración de consolas protegido con autenticación."""

    model = Consola
    template_name = 'consolas/gestionar.html'
    context_object_name = 'productos'


class ConsolaCreateView(LoginRequiredMixin, CreateView):
    model = Consola
    form_class = ConsolaForm
    template_name = 'consolas/consola_form.html'
    success_url = reverse_lazy('gestionar_consolas')
    extra_context = {'titulo': 'Agregar Consola / Mando'}


class ConsolaUpdateView(LoginRequiredMixin, UpdateView):
    model = Consola
    form_class = ConsolaForm
    template_name = 'consolas/consola_form.html'
    slug_field = 'hardware_id'
    slug_url_kwarg = 'hardware_id'
    success_url = reverse_lazy('gestionar_consolas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f'Editar: {self.object.nombre}'
        return context


class ConsolaDeleteView(LoginRequiredMixin, DeleteView):
    model = Consola
    template_name = 'consolas/consola_confirm_delete.html'
    context_object_name = 'producto'
    slug_field = 'hardware_id'
    slug_url_kwarg = 'hardware_id'
    success_url = reverse_lazy('gestionar_consolas')
