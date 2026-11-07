from django import template

register = template.Library()


@register.filter
def clp(value):
    """Formatea un número como peso chileno: 10000 -> $10.000."""
    try:
        numero = int(round(float(value)))
    except (TypeError, ValueError):
        return value
    return '$' + f'{numero:,}'.replace(',', '.')
