from ..models import Post,Category
from django import template

register = template.Library()   #register的名字是固定的,不可改变

@register.simple_tag
def get_recent_post(num=5):
    return Post.objects.all().order_by('-created_timestamp')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_timestamp','month',order='DESC')

@ register.simple_tag
def get_categories():
    return Category.objects.all()
    