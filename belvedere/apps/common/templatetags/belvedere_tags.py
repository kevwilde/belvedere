from django import template

register = template.Library()


@register.filter(name='lookup')
def dict_lookup(value, arg):
    return value[arg]
