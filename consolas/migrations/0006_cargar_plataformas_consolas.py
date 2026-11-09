from django.db import migrations


# Plataformas que se agregan al catálogo de consolas para que el formulario de
# videojuegos tenga una lista amplia donde elegir. Quedan con stock y precio 0:
# sirven como plataforma y no se muestran en el catálogo público de venta.
PLATAFORMAS = [
    ('nes', 'Nintendo Entertainment System (NES)', 1983),
    ('snes', 'Super Nintendo (SNES)', 1990),
    ('nintendo-64', 'Nintendo 64', 1996),
    ('gamecube', 'Nintendo GameCube', 2001),
    ('wii', 'Nintendo Wii', 2006),
    ('wii-u', 'Nintendo Wii U', 2012),
    ('nintendo-switch', 'Nintendo Switch', 2017),
    ('gameboy', 'Nintendo Game Boy', 1989),
    ('gameboy-color', 'Nintendo Game Boy Color', 1998),
    ('gameboy-advance', 'Nintendo Game Boy Advance', 2001),
    ('nintendo-ds', 'Nintendo DS', 2004),
    ('nintendo-3ds', 'Nintendo 3DS', 2011),
    ('playstation-1', 'PlayStation (PS1)', 1994),
    ('psp', 'PlayStation Portable (PSP)', 2004),
    ('ps-vita', 'PlayStation Vita', 2011),
    ('xbox-one', 'Xbox One', 2013),
    ('xbox-series', 'Xbox Series X/S', 2020),
    ('sega-master-system', 'SEGA Master System', 1985),
    ('game-gear', 'SEGA Game Gear', 1990),
    ('sega-saturn', 'SEGA Saturn', 1994),
    ('dreamcast', 'SEGA Dreamcast', 1998),
    ('atari-2600', 'Atari 2600', 1977),
    ('atari-5200', 'Atari 5200', 1982),
    ('atari-7800', 'Atari 7800', 1986),
    ('atari-jaguar', 'Atari Jaguar', 1993),
    ('neo-geo', 'Neo Geo', 1990),
    ('turbografx-16', 'TurboGrafx-16 / PC Engine', 1987),
    ('3do', '3DO Interactive Multiplayer', 1993),
    ('pc', 'PC / Steam', 1980),
    ('arcade', 'Arcade', 1971),
]


def cargar_plataformas(apps, schema_editor):
    Consola = apps.get_model('consolas', 'Consola')
    for hardware_id, nombre, ano in PLATAFORMAS:
        Consola.objects.get_or_create(
            hardware_id=hardware_id,
            defaults={
                'nombre': nombre,
                'stock': 0,
                'color': 'N/A',
                'estado': 'Plataforma',
                'ano': ano,
                'pilas': 'no',
                'controles': None,
                'descripcion': (
                    'Plataforma disponible para asociar videojuegos. '
                    'No está publicada para la venta.'
                ),
                'precio': 0,
                'imagen': '',
            },
        )


def eliminar_plataformas(apps, schema_editor):
    Consola = apps.get_model('consolas', 'Consola')
    Consola.objects.filter(
        hardware_id__in=[p[0] for p in PLATAFORMAS]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('consolas', '0005_alter_consola_precio'),
    ]

    operations = [
        migrations.RunPython(cargar_plataformas, eliminar_plataformas),
    ]
