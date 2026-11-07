from decimal import Decimal, ROUND_HALF_UP

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from consolas.models import Consola


class Videojuego(models.Model):
    nombre = models.CharField(max_length=200)
    stock = models.PositiveIntegerField(default=0)
    consola = models.ForeignKey(
        Consola,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='videojuegos',
        verbose_name='Consola compatible (opcional)',
    )
    consola_manual = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Nombre de la consola (si no está en la lista)',
        help_text='Si el juego se vende de forma independiente, escribe aquí la plataforma. Ej: PC, Nintendo 64, Arcade.',
    )
    estado = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    PEGI = models.CharField(max_length=10)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField(
        verbose_name='Precio (CLP)',
        help_text='Precio en pesos chilenos, sin decimales.',
    )
    imagen = models.ImageField(upload_to='images/videojuegos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Videojuego'
        verbose_name_plural = 'Videojuegos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    @property
    def plataforma(self):
        """Nombre de la plataforma, ya sea la consola del catálogo o el texto libre."""
        if self.consola:
            return self.consola.nombre
        return self.consola_manual or 'Juego independiente'


class Paquete(models.Model):
    """Oferta opcional que combina una consola y un videojuego con descuento."""

    nombre = models.CharField(
        max_length=200,
        blank=True,
        help_text='Si lo dejas vacío se genera automáticamente con el nombre de ambos productos.',
    )
    consola = models.ForeignKey(
        Consola,
        on_delete=models.CASCADE,
        related_name='paquetes',
    )
    videojuego = models.ForeignKey(
        Videojuego,
        on_delete=models.CASCADE,
        related_name='paquetes',
    )
    descuento = models.PositiveIntegerField(
        default=15,
        validators=[MinValueValidator(1), MaxValueValidator(90)],
        help_text='Porcentaje de descuento sobre la suma de ambos productos (1 a 90).',
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Paquete'
        verbose_name_plural = 'Paquetes'
        ordering = ['-fecha_creacion']

    @property
    def titulo(self):
        return self.nombre or f'{self.consola.nombre} + {self.videojuego.nombre}'

    @property
    def precio_base(self):
        return self.consola.precio + self.videojuego.precio

    @property
    def precio_final(self):
        factor = (Decimal('100') - Decimal(self.descuento)) / Decimal('100')
        return (self.precio_base * factor).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

    @property
    def ahorro(self):
        return self.precio_base - self.precio_final

    def __str__(self):
        return self.titulo
