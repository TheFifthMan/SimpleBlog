from django.shortcuts import render,reverse
from django.views.generic import ListView,View
import markdown 
from .models import  Post
# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class DetailView(View):
    def get(self,request,pk):
        post = Post.objects.get_object_or_404(pk=pk)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                      ])
        return render(request,'blog/single.html',{"post":post})

    