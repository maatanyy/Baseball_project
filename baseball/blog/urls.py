from django.urls import path, reverse, reverse_lazy
from . import views
from .models import *

app_name = 'blog'

urlpatterns = [
    path('', views.list, name='list'),
    path('new/',views.create, name='create'),
    path('<int:no>/',views.detail, name='detail'),
]
