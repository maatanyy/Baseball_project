from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .models import *
# Create your views here.

def test(request):
    
    store_list = Store.objects.filter(name__icontains='민')
    
    return render(request,'store/test.html',{'store_list': store_list})