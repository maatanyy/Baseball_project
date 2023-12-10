from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .models import *
from .forms import *
from accounts.models import MyUser
from django.contrib.auth.decorators import login_required

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

def post_update(request, id):
    
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance = post)
        
        if form.is_valid(): 
            form.save()
            return redirect('blog:list')
        
    else:
        form = PostModelForm(instance=post)
    
    return render(request, 'blog/post_update.html', {'form':form})
        

def post_delete(request, id):
    
    post = get_object_or_404(Post, id=id)
    
    if request.method =='POST':
        post.delete()
        return redirect('blog:list')
    
    else:
        return render(request, 'blog/post_delete.html',{'post':post})


def detail(request,no):
    post = get_object_or_404(Post, id=no)
    comment_list = post.comments.all()
    tag_list = post.tag.all()
    
    return render(request, 'blog/post_detail.html',{'post':post, 'comment_list':comment_list, 'tag_list':tag_list})    


def profile(request):
    user = request.user
    
    return render(request, 'blog/profile.html', {'user':user})

    
def tag_list(request, id):
    
    tag = Tag.objects.all(id=id)
    
    post_list = tag.post_set.all()
    
    return render(request,'blog/list.html',{'post_all': post_list})


    
    
    