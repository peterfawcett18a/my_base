from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all occurences of "arg" from the string.
    """
    return value.replace(arg,'')
