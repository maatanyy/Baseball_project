from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.contrib.auth.models import  AbstractUser, Group, Permission
# Create your models here.

class MyUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=50, null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions'
    )


