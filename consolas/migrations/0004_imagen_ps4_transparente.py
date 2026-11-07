from django.db import migrations


def actualizar_ps4(apps, schema_editor):
    Consola = apps.get_model('consolas', 'Consola')
    Consola.objects.filter(hardware_id='playstation-4').update(
        imagen='images/consolas/ps4.png'
    )


def revertir_ps4(apps, schema_editor):
    Consola = apps.get_model('consolas', 'Consola')
    Consola.objects.filter(hardware_id='playstation-4').update(
        imagen='images/consolas/ps4.jpg'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('consolas', '0003_actualizar_imagenes_consolas'),
    ]

    operations = [
        migrations.RunPython(actualizar_ps4, revertir_ps4),
    ]
