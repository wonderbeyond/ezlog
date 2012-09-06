from django import template
from django.conf import settings

register = template.Library()

#get settings value
@register.assignment_tag
def get_setting(name):
    return getattr(settings, name, "")

