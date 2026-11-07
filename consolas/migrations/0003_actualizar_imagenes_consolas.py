from django.db import migrations


IMAGENES = {
    'playstation-4': 'images/consolas/ps4.png',
    'playstation-2': 'images/consolas/ps2.png',
    'xbox-360': 'images/consolas/xbox360.png',
    'sega-genesis': 'images/consolas/genesis.png',
}


def asignar_imagenes(apps, schema_editor):
    Consola = apps.get_model('consolas', 'Consola')
    for hardware_id, imagen in IMAGENES.items():
        Consola.objects.filter(hardware_id=hardware_id).update(imagen=imagen)


def quitar_imagenes(apps, schema_editor):
    Consola = apps.get_model('consolas', 'Consola')
    Consola.objects.filter(hardware_id__in=IMAGENES.keys()).update(imagen='')


class Migration(migrations.Migration):

    dependencies = [
        ('consolas', '0002_cargar_consolas_iniciales'),
    ]

    operations = [
        migrations.RunPython(asignar_imagenes, quitar_imagenes),
    ]
