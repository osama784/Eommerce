from django import template
from math import ceil

register = template.Library()


@register.filter(name="split")
def split(value, arg):
    return value.split(arg)

@register.filter
def subtract(value, arg):
    return value - arg



