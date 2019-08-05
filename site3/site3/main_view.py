#创建视图函数的文件
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def rvs(request):
    # 使用reverse（） 反向解析url地址
    # 该方法必须传递一个参数，视图的名字，即url()函数的第三个参数name用于命名视图的名字
    #得到书首页的url地址
    # url = reverse("book:index")
    # 带参数的url地址
    # url = reverse("书详情页",args=['123']) #位置参数
    # url = reverse("book:书详情页",kwargs={"bid":999}) #关键字参数
    # url = reverse("movie:index")
    url = reverse("xiangqing")
    return HttpResponse("反向路由解析出来的地址：{}".format(url))

def test(request,bid):
    url = reverse("book:书详情页",kwargs={"bid" : bid})
    print(url)
    # return HttpResponse("跳转")
    return redirect(url)

def index(request):

    # return HttpResponse(f"index")
    return render(request,'index.html')

def detail(request,id,category):
    #位置参数  必须严格按照参数顺序来对应查值

    # return  HttpResponse(f"{category}类页面：id={id}")
    #命名参数，参数顺序无关紧要
    return  HttpResponse(f"id={id},类别={category}")