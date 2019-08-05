from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("电影首页")
def detail(request,mid):
    return HttpResponse(f"{mid}电影详情")