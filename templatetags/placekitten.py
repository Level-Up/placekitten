from django.contrib.auth.models import User
from classytags.core import Tag, Options
from classytags.arguments import Argument
from django import template


register = template.Library()


class placekitten(Tag):
    """
    Show a place-holder image from 
    placekitten.com
    
    Usage:
    {% placekitten 200 350 %}
    {% placekitten 200 350 "b&w" %}
    
    """

    options = Options(
        Argument('width', required=True),
        Argument('height', required=True),
        Argument('color', required=False),
    )

    def render_tag(self, context, width, height, color):
        host = "http://placekitten.com/g/" if color else "http://placekitten.com/"
        url = "%s%d/%d" % (host, width, height)
                
        return '<img src="%s" width="%d" height="%d" alt="I can haz placeholder?" />' % (url, width, height)

register.tag(placekitten)
