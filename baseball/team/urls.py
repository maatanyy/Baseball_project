from django.urls import path
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from . import views
from .models import *

app_name = 'team'

urlpatterns = [
    path('', TemplateView.as_view(template_name='team/team_list.html'), name='list'),
    path('list/', ListView.as_view(model=Team), name='team'),
    path('detail/<pk>/', DetailView.as_view(model=Team), name = 'team_detail'),
    path('add/', CreateView.as_view(model=Team, fields='__all__'), name='team_add'),
]
