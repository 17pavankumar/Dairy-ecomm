from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.views import View
# Create your views here.
def home(request):
    return render(request,"app/home.html")

def category(request):
    return render(request,"app/category.html")