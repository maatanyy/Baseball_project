from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
from . models import *
from . forms import *
# Create your views here.


def test1(request):
    
    return HttpResponse("hello")