from decimal import Decimal

from django.db import migrations


CONSOLAS = [
    {
        'hardware_id': 'mando-xbox360',
        'nombre': 'Mando de Xbox 360 Original',
        'stock': 12,
        'color': 'Negro',
        'estado': 'Nuevo',
        'ano': 2005,
        'pilas': '2',
        'controles': None,
        'descripcion': 'Mando clásico, compatible con PC para tus emuladores o juegos de Steam, tambien puedes jugar en la consola origial',
        'precio': Decimal('69000'),
        'imagen': 'images/consolas/xbox360.png',
    },
    {
        'hardware_id': 'nintendo-switch-oled',
        'nombre': 'Nintendo Switch Oled',
        'stock': 6,
        'color': 'Blanco',
        'estado': 'Nuevo',
        'ano': 2021,
        'pilas': 'no',
        'controles': 2,
        'descripcion': 'Consola Familiar de nintendo, penultima generacion de consolas, 2 mandos',
        'precio': Decimal('349000'),
        'imagen': 'images/consolas/nintendo_switch.png',
    },
    {
        'hardware_id': 'gameboy-sp',
        'nombre': 'Nintendo GameBoy Advance SP Pikachu Edition',
        'stock': 4,
        'color': 'amarillo',
        'estado': 'Como Nuevo',
        'ano': 2003,
        'pilas': 'no',
        'controles': None,
        'descripcion': 'Consola de nintendo, una joya de consola, creada al inicio de 2003, es una edicion especial de pokémon',
        'precio': Decimal('199000'),
        'imagen': 'images/consolas/gameboy-pika.jpg',
    },
    {
        'hardware_id': 'play3-slim',
        'nombre': 'Play Station 3 Slim',
        'stock': 7,
        'color': 'Negra',
        'estado': 'Poco Usado',
        'ano': 2009,
        'pilas': 'no',
        'controles': 2,
        'descripcion': 'Consola de gamer clasico, 2 mandos, puedes jugar muchos juegos FPS, singleplayer',
        'precio': Decimal('149000'),
        'imagen': 'images/consolas/ps3_slim.png',
    },
    {
        'hardware_id': 'virtual-boy',
        'nombre': 'Virtual Boy',
        'stock': 6,
        'color': 'Rojo',
        'estado': 'Como Nuevo',
        'ano': 1995,
        'pilas': '6',
        'controles': 2,
        'descripcion': 'Consola muy retro y de nicho de nintendo, como VR pero rojos, no puedes moverte con la cabeza, si no con el control',
        'precio': Decimal('899000'),
        'imagen': 'images/consolas/virtual_boy.png',
    },
    {
        'hardware_id': 'play5-d',
        'nombre': 'Play Station 5 Digital',
        'stock': 9,
        'color': 'Blanco',
        'estado': 'Nuevo',
        'ano': 2020,
        'pilas': 'no',
        'controles': 2,
        'descripcion': 'Consola competitiva para gamers que buscan disfrutar a tope los juegos por sus graficos',
        'precio': Decimal('649000'),
        'imagen': 'images/consolas/ps5.png',
    },
    {
        'hardware_id': 'mando-sega',
        'nombre': 'Mando SEGA Genesis',
        'stock': 2,
        'color': 'negro',
        'estado': 'Como Nuevo',
        'ano': 1988,
        'pilas': 'no',
        'controles': 2,
        'descripcion': 'Consola Familiar de Sega, joya retro, pefecta si eres collecionista, 2 mandos',
        'precio': Decimal('49000'),
        'imagen': 'images/consolas/genesis.png',
    },
    {
        'hardware_id': 'mando-play3',
        'nombre': 'Mando Play Station 3 Original',
        'stock': 4,
        'color': 'Negro',
        'estado': 'Nuevo',
        'ano': 2006,
        'pilas': 'no',
        'controles': None,
        'descripcion': 'Mando para jugar en la play station 3, original, nuevo',
        'precio': Decimal('19000'),
        'imagen': 'images/consolas/ps3.jpg',
    },
    {
        'hardware_id': 'xbox-classic',
        'nombre': 'Xbox Classic',
        'stock': 1,
        'color': 'Negro',
        'estado': 'Como Nuevo',
        'ano': 2001,
        'pilas': 'no',
        'controles': None,
        'descripcion': 'Consola retro, primera consola de microsoft, xbox clasica',
        'precio': Decimal('199000'),
        'imagen': 'images/consolas/xbox_classic.png',
    },
    # Plataformas adicionales usadas por los videojuegos iniciales
    {
        'hardware_id': 'playstation-4',
        'nombre': 'PlayStation 4',
        'stock': 10,
        'color': 'Negra',
        'estado': 'Nuevo',
        'ano': 2013,
        'pilas': 'no',
        'controles': 1,
        'descripcion': 'Consola de octava generación de Sony, ideal para jugar los grandes títulos de la década.',
        'precio': Decimal('299000'),
        'imagen': '',
    },
    {
        'hardware_id': 'playstation-2',
        'nombre': 'PlayStation 2',
        'stock': 8,
        'color': 'Negra',
        'estado': 'Como Nuevo',
        'ano': 2000,
        'pilas': 'no',
        'controles': 1,
        'descripcion': 'La consola más vendida de la historia, con un catálogo enorme de clásicos.',
        'precio': Decimal('129000'),
        'imagen': '',
    },
    {
        'hardware_id': 'xbox-360',
        'nombre': 'Xbox 360',
        'stock': 5,
        'color': 'Blanca',
        'estado': 'Poco Usado',
        'ano': 2005,
        'pilas': 'no',
        'controles': 1,
        'descripcion': 'Consola de séptima generación de Microsoft, con grandes sagas de acción y deportes.',
        'precio': Decimal('149000'),
        'imagen': '',
    },
    {
        'hardware_id': 'sega-genesis',
        'nombre': 'SEGA Genesis',
        'stock': 3,
        'color': 'Negra',
        'estado': 'Como Nuevo',
        'ano': 1988,
        'pilas': 'no',
        'controles': 1,
        'descripcion': 'Consola de 16 bits de SEGA, ícono de la era dorada de los videojuegos.',
        'precio': Decimal('129000'),
        'imagen': '',
    },
]


def cargar_consolas(apps, schema_editor):
    Consola = apps.get_model('consolas', 'Consola')
    for datos in CONSOLAS:
        Consola.objects.get_or_create(
            hardware_id=datos['hardware_id'],
            defaults=datos,
        )


def eliminar_consolas(apps, schema_editor):
    Consola = apps.get_model('consolas', 'Consola')
    Consola.objects.filter(
        hardware_id__in=[d['hardware_id'] for d in CONSOLAS]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('consolas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_consolas, eliminar_consolas),
    ]
