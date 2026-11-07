from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .filters import VideojuegoFilter
from .forms import PaqueteForm, VideojuegoForm
from .models import Paquete, Videojuego


class VideojuegoListView(ListView):
    """Catálogo público con filtros dinámicos conectados al ORM."""

    model = Videojuego
    template_name = 'videojuegos/videojuegos.html'
    context_object_name = 'productos'
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset().select_related('consola')
        # Conectamos request.GET con el FilterSet
        self.filterset = VideojuegoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pasamos el formulario de filtros al template
        context['form'] = self.filterset.form
        return context


class VideojuegoDetailView(DetailView):
    model = Videojuego
    template_name = 'videojuegos/detalle.html'
    context_object_name = 'producto'

    def get_queryset(self):
        return super().get_queryset().select_related('consola')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paquetes'] = self.object.paquetes.filter(activo=True).select_related(
            'consola'
        )
        return context


class VideojuegoManageListView(LoginRequiredMixin, ListView):
    """Panel de administración protegido con autenticación."""

    model = Videojuego
    template_name = 'videojuegos/gestionar.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return super().get_queryset().select_related('consola')


class VideojuegoCreateView(LoginRequiredMixin, CreateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'videojuegos/videojuego_form.html'
    success_url = reverse_lazy('gestionar_videojuegos')
    extra_context = {'titulo': 'Agregar Videojuego'}


class VideojuegoUpdateView(LoginRequiredMixin, UpdateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'videojuegos/videojuego_form.html'
    success_url = reverse_lazy('gestionar_videojuegos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f'Editar Videojuego: {self.object.nombre}'
        return context


class VideojuegoDeleteView(LoginRequiredMixin, DeleteView):
    model = Videojuego
    template_name = 'videojuegos/eliminar.html'
    context_object_name = 'producto'
    success_url = reverse_lazy('gestionar_videojuegos')


# ---------------------------------------------------------------------------
# Paquetes / Ofertas (consola + videojuego con descuento)
# ---------------------------------------------------------------------------


class PaqueteManageListView(LoginRequiredMixin, ListView):
    """Panel de administración de paquetes."""

    model = Paquete
    template_name = 'videojuegos/gestionar_paquetes.html'
    context_object_name = 'paquetes'

    def get_queryset(self):
        return super().get_queryset().select_related('consola', 'videojuego')


class PaqueteCreateView(LoginRequiredMixin, CreateView):
    model = Paquete
    form_class = PaqueteForm
    template_name = 'videojuegos/paquete_form.html'
    success_url = reverse_lazy('gestionar_paquetes')
    extra_context = {'titulo': 'Agregar Paquete / Oferta'}


class PaqueteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paquete
    form_class = PaqueteForm
    template_name = 'videojuegos/paquete_form.html'
    success_url = reverse_lazy('gestionar_paquetes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f'Editar Paquete: {self.object.titulo}'
        return context


class PaqueteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paquete
    template_name = 'videojuegos/paquete_confirm_delete.html'
    context_object_name = 'paquete'
    success_url = reverse_lazy('gestionar_paquetes')
