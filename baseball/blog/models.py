from django.db import models
from django.urls import reverse, reverse_lazy
from accounts.models import MyUser

# Create your models here.

class Post(models.Model):
    
    def __str__(self):
        return self.title  
    
    title = models.CharField(max_length=250)
    body = models.TextField()
    tag = models.ManyToManyField('Tag', null=True, blank=True)
    ip = models.GenericIPAddressField(null=True)
    
    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])
    


class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name='comments')
    author = models.CharField(max_length=20)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=True)
    

class Tag(models.Model):
    
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    

class Profile(models.Model):
    
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE,related_name='profile')
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    
    
    