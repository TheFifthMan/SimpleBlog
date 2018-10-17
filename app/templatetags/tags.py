from ..models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()   #register的名字是固定的,不可改变

@register.simple_tag
def get_recent_post(num=5):
    return Post.objects.all().order_by('-created_timestamp')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_timestamp','month',order='DESC')

@ register.simple_tag
def get_categories():
    return Category.objects.annotate(num=Count('posts')).filter(num__gt=0)
    
@register.simple_tag
def get_tags():
    # posts 取自related_name
    return Tag.objects.annotate(num=Count('posts')).filter(num__gt=0)