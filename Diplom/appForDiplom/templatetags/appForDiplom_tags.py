from django import template

from appForDiplom.models import Lessons

register = template.Library()

@register.simple_tag(name='get_list_lessons')
def get_categories():
    return Lessons.objects.all()


@register.inclusion_tag('appForDiplom/list_lessons.html')
def show_categories():
    categories = get_categories()
    return {"categories": categories}