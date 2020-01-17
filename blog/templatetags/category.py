from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag("tags/category.html")
def list_category():
    return {"categories" : Category.objects.all()}
