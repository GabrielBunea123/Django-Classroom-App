import random

from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def random_img():
    choices = []
    for i in range(2,11):
        choices.append(f"images/studies{i}.jpg")
    return random.choice(choices)
