from django import forms

from .models import Paquete, Videojuego


class VideojuegoForm(forms.ModelForm):
    precio = forms.CharField(
        label='Precio en pesos chilenos (CLP)',
        widget=forms.TextInput(
            attrs={'inputmode': 'numeric', 'placeholder': 'Ej: 29.000'}
        ),
    )

    class Meta:
        model = Videojuego
        fields = [
            'nombre',
            'stock',
            'consola',
            'consola_manual',
            'estado',
            'ano',
            'PEGI',
            'descripcion',
            'precio',
            'imagen',
        ]
        labels = {
            'nombre': 'Nombre del videojuego',
            'stock': 'Stock (unidades disponibles)',
            'consola': 'Consola compatible (opcional)',
            'consola_manual': 'Nombre de la consola escrito a mano',
            'estado': 'Estado del producto',
            'ano': 'Año de lanzamiento',
            'PEGI': 'Clasificación PEGI',
            'descripcion': 'Descripción',
            'precio': 'Precio en pesos chilenos (CLP)',
            'imagen': 'Imagen',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'nombre': 'Ej: Minecraft',
            'stock': 'Ej: 15',
            'consola_manual': 'Ej: PC, Nintendo 64, Arcade...',
            'estado': 'Ej: Nuevo',
            'ano': 'Ej: 2020',
            'PEGI': 'Ej: +13',
            'descripcion': 'Describe el videojuego aquí...',
            'precio': 'Ej: 29.000',
        }
        ayudas = {
            'nombre': 'Escribe el título del juego tal como aparece en su portada. Sirve para encontrarlo fácilmente en el catálogo.',
            'stock': 'Cantidad de unidades que hay para vender. Escribe solo números, sin puntos ni espacios.',
            'consola': 'Opcional. Si el juego es compatible con una consola del catálogo, selecciónala. Si no aparece en la lista, déjala en "Sin consola" y escribe el nombre a mano abajo.',
            'consola_manual': 'Solo si no seleccionaste una consola del catálogo. Escribe la plataforma a mano. Si lo dejas vacío, el juego se mostrará como "Juego independiente".',
            'estado': 'En qué condición está el producto. Opciones: Nuevo, Como Nuevo, Poco Usado, Usado.',
            'ano': 'Año en que salió a la venta. Solo 4 números, por ejemplo: 2020.',
            'PEGI': 'Clasificación de edad recomendada. Ejemplos: +3, +7, +12, +16, +18.',
            'descripcion': 'Cuenta brevemente de qué trata el juego, su modo de juego o por qué vale la pena. Entre 1 y 3 frases está bien.',
            'precio': 'Precio en pesos chilenos, sin decimales. Puedes escribirlo con o sin puntos: 29.000 o 29000.',
            'imagen': 'Opcional. Elige una imagen guardada en tu computador (JPG o PNG) y se subirá sola.',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]
            if field_name in ayudas:
                field.help_text = ayudas[field_name]
        self.fields['consola'].empty_label = 'Sin consola (venta independiente)'

    def clean_precio(self):
        """Acepta 29000 o 29.000 y lo guarda como entero en pesos."""
        valor = self.cleaned_data.get('precio')
        if isinstance(valor, int):
            return valor
        limpio = str(valor).replace('.', '').replace('$', '').replace(' ', '')
        if not limpio.isdigit():
            raise forms.ValidationError(
                'Escribe solo números enteros. Ejemplo: 29000 o 29.000.'
            )
        return int(limpio)

    def clean(self):
        cleaned = super().clean()
        # Si se eligió una consola del catálogo, el texto libre no es necesario
        if cleaned.get('consola'):
            cleaned['consola_manual'] = ''
        return cleaned


class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ['nombre', 'consola', 'videojuego', 'descuento', 'activo']
        labels = {
            'nombre': 'Nombre del paquete (opcional)',
            'consola': 'Consola del paquete',
            'videojuego': 'Videojuego del paquete',
            'descuento': 'Descuento (%)',
            'activo': 'Mostrar en la página de inicio',
        }
        widgets = {
            'descuento': forms.NumberInput(attrs={'min': 1, 'max': 90}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'nombre': 'Ej: Combo PS5 + Cyberpunk',
            'descuento': 'Ej: 15',
        }
        ayudas = {
            'nombre': 'Si lo dejas vacío, se generará automáticamente como "Consola + Videojuego".',
            'consola': 'Selecciona la consola que se incluye en la oferta.',
            'videojuego': 'Selecciona el juego que se incluye en la oferta.',
            'descuento': 'Porcentaje de descuento sobre la suma de ambos productos. Por defecto 15%.',
            'activo': 'Si está marcado, el paquete aparecerá en la sección de ofertas del inicio.',
        }
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]
            if field_name in ayudas:
                field.help_text = ayudas[field_name]
