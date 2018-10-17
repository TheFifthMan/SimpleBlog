from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
import markdown


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name='文章类名')

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'category'
        verbose_name = '文章种类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=50,verbose_name='标签名')

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'tag'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name


class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    created_timestamp = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    modified_timestamp = models.DateTimeField(blank=True,verbose_name="修改时间")
    excerpt = models.CharField(max_length=250,blank=True,null=True,verbose_name='内容摘要')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='posts',verbose_name="种类")
    tags = models.ManyToManyField('Tag',blank=True,verbose_name='文章标签',related_name='posts')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts',verbose_name='作者')
    views = models.IntegerField(default=0,verbose_name="阅读量")

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("app:detail", kwargs={"pk": self.pk})

    def save(self,*args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        
        super(Post, self).save(*args, **kwargs)


    class Meta:
        db_table = 'post'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_timestamp']

class Comment(models.Model):
    username = models.CharField(max_length=50,verbose_name='username')
    email = models.EmailField(verbose_name='email')
    url = models.URLField(verbose_name="url",blank=True, null=True)
    content = models.TextField(verbose_name="comment")
    created_timestamp = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('app.Post',on_delete=models.CASCADE,related_name="comment",verbose_name="对应的文章")


    def __str__(self):
        return self.content
    
    class Meta:
        db_table = "comment"
        verbose_name = "评论"
        verbose_name_plural = verbose_name


