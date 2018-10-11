from django.urls import path,re_path
from .views import IndexView,DetailView

app_name = 'app'
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    re_path(r'^post/(?P<pk>[0-9]+$)',DetailView.as_view(),name='detail')
]