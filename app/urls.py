from django.urls import path,re_path
from .views import IndexView,DetailView,ArchivesView,CategoriesView,TagsView
from .feeds import RSSFeed

# 有时候其他的app也会出现detail这样的名字，这个时候幼加一个app_name加以区别，用法为app:detail
app_name = 'app'
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    re_path(r'^post/(?P<pk>[0-9]+$)',DetailView.as_view(),name='detail'),
    re_path(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]{1,2})$',ArchivesView.as_view(),name='archives'),
    re_path(r'^category/(?P<pk>[0-9]+$)',CategoriesView.as_view(),name='category'),
    re_path(r'^tag/(?P<pk>[0-9]+)$',TagsView.as_view(),name='tag'),
    path('all/rss/',RSSFeed(),name='rss'),
]