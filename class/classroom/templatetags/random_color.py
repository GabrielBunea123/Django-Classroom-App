import random

from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def random_clr():
    choices = ['primary','warning','secondary','success','danger','info']
    return random.choice(choices)