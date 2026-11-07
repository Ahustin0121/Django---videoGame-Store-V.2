from django.db import models


class Consola(models.Model):
    hardware_id = models.SlugField(max_length=100, unique=True)
    nombre = models.CharField(max_length=150)
    stock = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    pilas = models.CharField(max_length=20, blank=True, null=True)
    controles = models.PositiveIntegerField(blank=True, null=True)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField(
        verbose_name='Precio (CLP)',
        help_text='Precio en pesos chilenos, sin decimales.',
    )
    imagen = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Consola'
        verbose_name_plural = 'Consolas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
