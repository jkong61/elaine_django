from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    attrs = {}
    attrs['class'] = css

    return field.as_widget(attrs=attrs)