from decimal import Decimal

from django.db import migrations


VIDEOJUEGOS = [
    {
        'nombre': 'Red Dead Redemption 2',
        'stock': 20,
        'consola': 'playstation-4',
        'estado': 'Nuevo',
        'ano': 2018,
        'PEGI': '+18',
        'descripcion': 'Juego de acción y aventura en un vasto mundo abierto desarrollado por Rockstar Games.',
        'precio': Decimal('29000'),
        'imagen': 'images/videojuegos/red.png',
    },
    {
        'nombre': 'Cyberpunk 2077',
        'stock': 21,
        'consola': 'play5-d',
        'estado': 'Nuevo',
        'ano': 2022,
        'PEGI': '+18',
        'descripcion': 'Un juego de rol de acción y mundo abierto ambientado en la futurista y peligrosa megalópolis de Night City',
        'precio': Decimal('39000'),
        'imagen': 'images/videojuegos/cyber.png',
    },
    {
        'nombre': 'The Legend Of Zelda Tears Of The Kingdom',
        'stock': 20,
        'consola': 'nintendo-switch-oled',
        'estado': 'Nuevo',
        'ano': 2023,
        'PEGI': '+10',
        'descripcion': 'Videojuego de acción y aventura en mundo abierto desarrollado por Nintendo, Link y la Princesa Zelda investigan un misterio bajo el Castillo de Hyrule',
        'precio': Decimal('59000'),
        'imagen': 'images/videojuegos/tloz.jpeg',
    },
    {
        'nombre': 'Guitar Hero 2',
        'stock': 10,
        'consola': 'playstation-2',
        'estado': 'Como Nuevo',
        'ano': 2006,
        'PEGI': '+12',
        'descripcion': 'Videojuego de ritmo musical desarrollado por Harmonix, usas el mando para pulsar los trastes de colores al ritmo del ROCK',
        'precio': Decimal('19000'),
        'imagen': 'images/videojuegos/gh2.png',
    },
    {
        'nombre': 'Guitar Hero 3',
        'stock': 10,
        'consola': 'xbox-360',
        'estado': 'Como Nuevo',
        'ano': 2007,
        'PEGI': '+12',
        'descripcion': 'Juego de ritmo y música lanzado en octubre de 2007, desarrollado por Neversoft y publicado por Activision. Luego de sus 2 juegos anteriores guitar hero 2 y guitar hero 1',
        'precio': Decimal('19000'),
        'imagen': 'images/videojuegos/gh3.png',
    },
    {
        'nombre': 'Silent Hills 3',
        'stock': 20,
        'consola': 'playstation-2',
        'estado': 'Como Nuevo',
        'ano': 2003,
        'PEGI': '+18',
        'descripcion': 'Videojuego de terror psicológico y supervivencia. La protagonista es Heather Mason, una adolescente común que lleva una vida tranquila. De repente, Heather queda atrapada en una pesadilla llena de monstruos y realidades alternativas.',
        'precio': Decimal('79000'),
        'imagen': 'images/videojuegos/sh3.png',
    },
    {
        'nombre': 'Sonic hedgehog',
        'stock': 4,
        'consola': 'sega-genesis',
        'estado': 'Poco Usado',
        'ano': 1991,
        'PEGI': '+6',
        'descripcion': 'Un clásico videojuego de plataformas desarrollado por Sega. Sonic, un erizo azul que corre a velocidades supersónicas.',
        'precio': Decimal('89000'),
        'imagen': 'images/videojuegos/sonic.jpeg',
    },
]


def cargar_videojuegos(apps, schema_editor):
    Consola = apps.get_model('consolas', 'Consola')
    Videojuego = apps.get_model('videojuegos', 'Videojuego')

    for datos in VIDEOJUEGOS:
        datos = dict(datos)
        hardware_id = datos.pop('consola')
        consola = Consola.objects.get(hardware_id=hardware_id)
        Videojuego.objects.get_or_create(
            nombre=datos['nombre'],
            defaults={**datos, 'consola': consola},
        )


def eliminar_videojuegos(apps, schema_editor):
    Videojuego = apps.get_model('videojuegos', 'Videojuego')
    Videojuego.objects.filter(
        nombre__in=[d['nombre'] for d in VIDEOJUEGOS]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('consolas', '0002_cargar_consolas_iniciales'),
        ('videojuegos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_videojuegos, eliminar_videojuegos),
    ]
