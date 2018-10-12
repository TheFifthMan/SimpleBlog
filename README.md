# SimpleBlog 
基于django搭建的简单博客系统。
# chapter3 - 功能实现
前面实现了路由和视图的配置，这里实现一下功能

## 1-展示的功能
```
1. 静态文件
所有的html和静态文件都要放在app里面。这样就无需做任何的处理，否则需要如下处理
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # 这里指明templates的位置
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                ...
            ],
        },
    },
]

STATIC_URL = '/static/' # 这里指明static的位置

2. 模板继承
{% extends "base.html" %}
{% block content %}{% endblock %}

3. 静态文件导入
{% load staticfiles %}
{% static 'css/xxx.css' %}
```
## 后台管理功能
```
python manage.py createsuperuser

# app/admin.py
from django.contrib import admin
from .models import Category,Post,Tag
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','excerpt','category','created_timestamp','modified_timestamp']

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)

```
## 文章详情页
```
get_object_or_404(models,pk=pk)
这个不是类的功能，是shortcut的功能
```

