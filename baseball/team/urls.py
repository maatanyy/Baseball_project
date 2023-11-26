from django.urls import path
from . import views

urlpatterns = [
    #path('team/', views.list, name = 'list'),
    path('test1/', views.test1, name='test1'),
]