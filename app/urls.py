from django.urls import path,re_path
from .views import IndexView,DetailView,ArchivesView,CategoriesView

app_name = 'app'
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    re_path(r'^post/(?P<pk>[0-9]+$)',DetailView.as_view(),name='detail'),
    re_path(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]{1,2})$',ArchivesView.as_view(),name='archives'),
    re_path(r'^category/(?P<pk>[0-9]+$)',CategoriesView.as_view(),name='category'),
]