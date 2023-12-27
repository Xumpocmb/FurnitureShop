from django import template
from catalog_app.models import Category

register = template.Library()


@register.simple_tag(name='tag_catalog')
def tag_catalog():
    return Category.objects.all()
