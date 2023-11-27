from django.urls import path, reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from . import views
from .models import *

app_name = 'team'

urlpatterns = [
    
    path('', ListView.as_view(model=Team), name = 'list'),
    path('detail/<pk>/', DetailView.as_view(model=Team), name = 'detail'),
    path('create/', CreateView.as_view(model=Team, fields ='__all__'), name='create'),
    path('update/<pk>/', UpdateView.as_view(model=Team, fields ='__all__'), name='update'),
    path('delete/<pk>/', DeleteView.as_view(model=Team, success_url = reverse_lazy('team:list')), name='delete'),
]
