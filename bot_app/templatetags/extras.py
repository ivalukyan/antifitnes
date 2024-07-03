from django import template

register = template.Library()


@register.filter
def getattr_safe(obj, attr):
    try:
        return getattr(obj, attr, '')
    except AttributeError:
        return ''
