from django.shortcuts import render,reverse,get_object_or_404,redirect,reverse
from django.views.generic import ListView,View
import markdown 
from .models import  Post,Category,Comment
from .forms import CommentModelForm
# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class DetailView(View):
    def get(self,request,pk):
        form = CommentModelForm()
        post = get_object_or_404(Post,pk=pk)
        post.content = markdown.markdown(post.content,
                                      extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                      ])
        post.increase_views()
        comments = post.comment.all().order_by('-created_timestamp') 
        return render(request,'blog/single.html',{"post":post,"comments":comments,"form":form})

    def post(self,request,pk):
        article = get_object_or_404(Post,pk=pk)
        print(article)
        form = CommentModelForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            email = request.POST.get('email','')
            url = request.POST.get('url','')
            body = request.POST.get('body',"")
            comment = Comment(username=username,email=email,url=url,content=body)
            comment.article = article 
            comment.save()
            return redirect(reverse("app:detail",args=[pk]))
        else:
            print(form.errors)
        comments = article.comment.all().order_by('-created_timestamp')  
        return render(request,'blog/single.html',{"post":article,'comments':comments,"form":form})




class ArchivesView(View):
    def get(self,request,year,month):
        posts = Post.objects.filter(created_timestamp__year=year,created_timestamp__month=month).order_by('-created_timestamp')
        return render(request,'blog/index.html',{"posts":posts})

class CategoriesView(View):
    def get(self,request,pk):
        category =get_object_or_404(Category,pk=pk)
        posts = Post.objects.filter(category=category).all()
        return render(request,'blog/index.html',{'posts':posts})

