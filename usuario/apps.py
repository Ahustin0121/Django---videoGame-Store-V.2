from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate


def crear_superusuarios(sender, **kwargs):
    from django.contrib.auth.models import User
    for datos in getattr(settings, 'SUPERUSUARIOS', []):
        if not User.objects.filter(username=datos['username']).exists():
            User.objects.create_superuser(
                username=datos['username'],
                email=datos['email'],
                password=datos['password'],
            )


class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuario'

    def ready(self):
        post_migrate.connect(crear_superusuarios, sender=self)