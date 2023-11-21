from django import template
from main.models import Tags

register = template.Library()


@register.simple_tag(name='news_tags')
def get_news_tags():
    return Tags.objects.all()
