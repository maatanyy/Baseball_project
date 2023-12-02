from django.urls import path, reverse, reverse_lazy
from . import views
from .models import *

app_name = 'blog'

urlpatterns = [
    path('', views.list, name='list'),
    path('new/',views.create, name='create'),
    path('<int:no>/',views.detail, name='detail'),
    path('profile/', views.profile),
    path('tag/<id>/',views.tag_list),
    path('update/<id>/', views.post_update, name='update'),
    path('delete/<id>/', views.post_delete, name='delete'),
]
