from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("图书首页")
def detail(request,bid):
    return HttpResponse(f"图书详情页：{bid}")
