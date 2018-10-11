# SimpleBlog 
基于django搭建的简单博客系统。
# chapter2 - 首页视图
## urls

```
# app/urls.py

from django.urls import path
from .views import IndexView

app_name = 'app'
urlpatterns = [
    path('',IndexView.as_view(),name='index')
]

# blog/urls.py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',include('app.urls')),
]

```
## views
```
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
```
