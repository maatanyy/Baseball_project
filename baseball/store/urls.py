from django.urls import path, reverse, reverse_lazy
from . import views
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *

app_name = 'store'

urlpatterns = [
    
    path('', ListView.as_view(model=Store), name = 'list'),

]
