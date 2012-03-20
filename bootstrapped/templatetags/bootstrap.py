from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def bootstrap_less(less):
    return '<script src="%sjs/less-1.1.5.min.js" type="text/javascript"></script>' % settings.STATIC_URL
