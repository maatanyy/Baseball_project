from django.db import models
from django.urls import path, reverse

# Create your models here.

class Team(models.Model):
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team:list')
    
    name = models.CharField(max_length=30)
    level = models.IntegerField()

    

class Member(models.Model):
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    position = models.CharField(max_length=20)
    staff = models.BooleanField()

    def __str__(self):
        return self.name