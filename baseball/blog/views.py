from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .models import *
from .forms import *

# Create your views here.

def list(request):
    post_list = Post.objects.all()
    
    return render(request, 'blog/list.html', {'post_all': post_list})

def create(request):
    
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            print('cleaned_data', form.cleaned_data)
            
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect(post)
        
    else:
        form = PostModelForm()
        
    return render(request, 'blog/post_form.html',{'form':form})

def detail(request,no):
    post = get_object_or_404(Post, id=no)
    comment_list = post.comments.all()
    tag_list = post.tag.all()
    
    return render(request, 'blog/detail.html',{'post':post, 'comment_list':comment_list, 'tag_list':tag_list})    
            
    
    
    