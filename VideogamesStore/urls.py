from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from consolas import views as consolas_views
from usuario.views import admin_login, admin_logout, contacto, inicio
from videojuegos import views as videojuegos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),

    # Autenticación
    path('adminlogin/', admin_login, name='admin_login'),
    path('adminlogout/', admin_logout, name='admin_logout'),

    # Consolas
    path('consola/', consolas_views.ConsolaListView.as_view(), name='consolas'),
    path(
        'consolas/gestionar/',
        consolas_views.ConsolaManageListView.as_view(),
        name='gestionar_consolas',
    ),
    path(
        'consolas/nuevo/',
        consolas_views.ConsolaCreateView.as_view(),
        name='crear_consola',
    ),
    path(
        'consolas/<slug:hardware_id>/',
        consolas_views.ConsolaDetailView.as_view(),
        name='detalle_consola',
    ),
    path(
        'consolas/<slug:hardware_id>/editar/',
        consolas_views.ConsolaUpdateView.as_view(),
        name='editar_consola',
    ),
    path(
        'consolas/<slug:hardware_id>/eliminar/',
        consolas_views.ConsolaDeleteView.as_view(),
        name='eliminar_consola',
    ),

    # Videojuegos
    path(
        'videojuegos/',
        videojuegos_views.VideojuegoListView.as_view(),
        name='videojuegos',
    ),
    path(
        'videojuegos/gestionar/',
        videojuegos_views.VideojuegoManageListView.as_view(),
        name='gestionar_videojuegos',
    ),
    path(
        'videojuegos/nuevo/',
        videojuegos_views.VideojuegoCreateView.as_view(),
        name='crear_videojuego',
    ),
    path(
        'videojuegos/editar/<int:pk>/',
        videojuegos_views.VideojuegoUpdateView.as_view(),
        name='editar_videojuego',
    ),
    path(
        'videojuegos/eliminar/<int:pk>/',
        videojuegos_views.VideojuegoDeleteView.as_view(),
        name='eliminar_videojuego',
    ),
    path(
        'videojuegos/<int:pk>/',
        videojuegos_views.VideojuegoDetailView.as_view(),
        name='detalle_videojuego',
    ),

    # Paquetes / Ofertas
    path(
        'paquetes/gestionar/',
        videojuegos_views.PaqueteManageListView.as_view(),
        name='gestionar_paquetes',
    ),
    path(
        'paquetes/nuevo/',
        videojuegos_views.PaqueteCreateView.as_view(),
        name='crear_paquete',
    ),
    path(
        'paquetes/editar/<int:pk>/',
        videojuegos_views.PaqueteUpdateView.as_view(),
        name='editar_paquete',
    ),
    path(
        'paquetes/eliminar/<int:pk>/',
        videojuegos_views.PaqueteDeleteView.as_view(),
        name='eliminar_paquete',
    ),

    # Contacto
    path('contacto/', contacto, name='contacto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
