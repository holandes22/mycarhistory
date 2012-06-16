from django import template

register = template.Library()

@register.filter()
def replace_under_with(value, arg):
    return value.replace("_", arg)

@register.filter()
def field_type(field):
    return field.field.__class__.__name__
