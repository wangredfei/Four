from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("这是index应用中的index访问路径")

def login(request):
    return HttpResponse("这是index应用中的login访问路径")

def register(request):
    return HttpResponse("这是index应用中的register访问路径")




