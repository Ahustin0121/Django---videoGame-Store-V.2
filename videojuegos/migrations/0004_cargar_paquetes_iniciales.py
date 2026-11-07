from django.db import migrations


PAQUETES = [
    {
        'consola': 'play5-d',
        'videojuego': 'Cyberpunk 2077',
        'nombre': 'Combo Next-Gen: PS5 + Cyberpunk 2077',
        'descuento': 15,
    },
    {
        'consola': 'nintendo-switch-oled',
        'videojuego': 'The Legend Of Zelda Tears Of The Kingdom',
        'nombre': 'Combo Nintendo: Switch OLED + Zelda TotK',
        'descuento': 15,
    },
    {
        'consola': 'playstation-4',
        'videojuego': 'Red Dead Redemption 2',
        'nombre': 'Combo Western: PS4 + Red Dead Redemption 2',
        'descuento': 15,
    },
    {
        'consola': 'sega-genesis',
        'videojuego': 'Sonic hedgehog',
        'nombre': 'Combo Retro: SEGA Genesis + Sonic',
        'descuento': 15,
    },
]


def cargar_paquetes(apps, schema_editor):
    Consola = apps.get_model('consolas', 'Consola')
    Videojuego = apps.get_model('videojuegos', 'Videojuego')
    Paquete = apps.get_model('videojuegos', 'Paquete')

    for datos in PAQUETES:
        consola = Consola.objects.filter(hardware_id=datos['consola']).first()
        videojuego = Videojuego.objects.filter(nombre=datos['videojuego']).first()
        if not consola or not videojuego:
            continue
        Paquete.objects.get_or_create(
            consola=consola,
            videojuego=videojuego,
            defaults={
                'nombre': datos['nombre'],
                'descuento': datos['descuento'],
                'activo': True,
            },
        )


def eliminar_paquetes(apps, schema_editor):
    Paquete = apps.get_model('videojuegos', 'Paquete')
    Paquete.objects.filter(nombre__in=[d['nombre'] for d in PAQUETES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('videojuegos', '0003_alter_videojuego_consola_paquete'),
        ('consolas', '0002_cargar_consolas_iniciales'),
    ]

    operations = [
        migrations.RunPython(cargar_paquetes, eliminar_paquetes),
    ]
