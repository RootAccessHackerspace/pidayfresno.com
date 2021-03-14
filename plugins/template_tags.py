import os
import random

import yaml

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_videos(context, varname):
    path = os.path.join(os.path.dirname(__file__), '../videos.yaml')
    with open(path, 'r') as f:
        context[varname] = yaml.safe_load(f.read())
    return ''


@register.simple_tag()
def random_wire(count):
    wires = [
        'Raspberry-Jam-Graphics_Jumper Lead FF 1.svg',
        'Raspberry-Jam-Graphics_Jumper Lead FF 2.svg',
        'Raspberry-Jam-Graphics_Jumper Lead FF 3.svg',
        'Raspberry-Jam-Graphics_Jumper Lead FM.svg',
        'Raspberry-Jam-Graphics_Jumper Lead MM 1.svg',
        'Raspberry-Jam-Graphics_Jumper Lead MM 2.svg',
    ]

    return f'/static/img/jam/{wires[count % len(wires)]}'
