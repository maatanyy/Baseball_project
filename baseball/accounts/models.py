from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    
    

