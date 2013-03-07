from django.conf import settings
from django import template

URCHIN_ID = getattr(settings, 'URCHIN_ID', None)
URCHIN_DEBUG = getattr(settings, 'URCHIN_DEBUG', False)
URCHIN_AUTOLOAD = getattr(settings, 'URCHIN_AUTOLOAD', True)

register = template.Library()

@register.inclusion_tag('urchin/track.html', name='urchin_track')
def do_track(id=URCHIN_ID):
    if id is None:
        raise template.TemplateSyntaxError, "Set URCHIN_ID in settings.py or pass GA tracking ID as argument."

    return {
        'URCHIN_ID': id,
        'URCHIN_AUTOLOAD': URCHIN_AUTOLOAD,
        'URCHIN_DEBUG': URCHIN_DEBUG,
    }

@register.inclusion_tag('urchin/load.html', name='urchin_load')
def do_load():
    return {
        'URCHIN_AUTOLOAD': URCHIN_AUTOLOAD,
        'URCHIN_DEBUG': URCHIN_DEBUG,
    }