# SimpleBlog 
基于django搭建的简单博客系统。
# chapter4
## 注册自定义标签
注册自定义标签有三个点需要遵守
1. INSTALL_APP 里面要有这个app的名字
2. 在app里面新建一个包：templatetags
3. 在包里面新建py文件
```
register = template.Library()   #register的名字是固定的,不可改变

@register.simple_tag
def get_recent_post(num=5):
    return Post.objects.all().order_by('-created_timestamp')[:num]
```
