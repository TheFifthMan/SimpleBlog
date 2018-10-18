from django.contrib.syndication.views import Feed
from .models import Post

class RSSFeed(Feed):
    title = 'simple blog'
    link = '/'

    def items(self):
        return Post.objects.all()

    def items_title(self,item):
        return "[{}] {}".format(item.category,item.title)

    def items_description(self,item):
        return item.content