from django import forms

from consolas.models import Consola


class ConsolaForm(forms.ModelForm):
    precio = forms.CharField(
        label='Precio en pesos chilenos (CLP)',
        widget=forms.TextInput(
            attrs={'inputmode': 'numeric', 'placeholder': 'Ej: 649.000'}
        ),
    )

    class Meta:
        model = Consola
        fields = [
            'hardware_id',
            'nombre',
            'stock',
            'color',
            'estado',
            'ano',
            'pilas',
            'controles',
            'descripcion',
            'precio',
            'imagen',
        ]
        labels = {
            'hardware_id': 'Identificador (slug)',
            'nombre': 'Nombre de la consola / mando',
            'stock': 'Stock (unidades disponibles)',
            'color': 'Color',
            'estado': 'Estado del producto',
            'ano': 'Año de lanzamiento',
            'pilas': 'Pilas requeridas',
            'controles': 'Controles incluidos',
            'descripcion': 'Descripción',
            'precio': 'Precio en pesos chilenos (CLP)',
            'imagen': 'Ruta de la imagen',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'hardware_id': 'Ej: play5-d',
            'nombre': 'Ej: Play Station 5 Digital',
            'stock': 'Ej: 9',
            'color': 'Ej: Blanco',
            'estado': 'Ej: Nuevo',
            'ano': 'Ej: 2020',
            'pilas': 'Ej: no',
            'controles': 'Ej: 2',
            'descripcion': 'Describe la consola o mando...',
            'precio': 'Ej: 649.000',
            'imagen': 'Ej: images/consolas/ps5.png',
        }
        ayudas = {
            'precio': 'Precio en pesos chilenos, sin decimales. Puedes escribirlo con o sin puntos: 649.000 o 649000.',
            'imagen': 'Escribe la ruta de una imagen dentro de static, por ejemplo: images/consolas/ps5.png.',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]
            if field_name in ayudas:
                field.help_text = ayudas[field_name]

    def clean_precio(self):
        """Acepta 649000 o 649.000 y lo guarda como entero en pesos."""
        valor = self.cleaned_data.get('precio')
        if isinstance(valor, int):
            return valor
        limpio = str(valor).replace('.', '').replace('$', '').replace(' ', '')
        if not limpio.isdigit():
            raise forms.ValidationError(
                'Escribe solo números enteros. Ejemplo: 649000 o 649.000.'
            )
        return int(limpio)
