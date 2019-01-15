from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def show(request):
    return HttpResponse("这是music应用中的show访问路径")
