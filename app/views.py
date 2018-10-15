from django.shortcuts import render,reverse,get_object_or_404
from django.views.generic import ListView,View
import markdown 
from .models import  Post,Category
# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class DetailView(View):
    def get(self,request,pk):
        post = get_object_or_404(Post,pk=pk)
        post.content = markdown.markdown(post.content,
                                      extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                      ])
        return render(request,'blog/single.html',{"post":post})


class ArchivesView(View):
    def get(self,request,year,month):
        posts = Post.objects.filter(created_timestamp__year=year,created_timestamp__month=month).order_by('-created_timestamp')
        return render(request,'blog/index.html',{"posts":posts})

class CategoriesView(View):
    def get(self,request,pk):
        category =get_object_or_404(Category,pk=pk)
        posts = Post.objects.filter(category=category).all()
        return render(request,'blog/index.html',{'posts':posts})
