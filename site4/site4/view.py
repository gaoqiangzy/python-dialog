from django.shortcuts import render
def index(request):
    content = {
        'phone':13767926369,
        'title': '网站首页',
        'items': ['足球','篮球','乒乓球','羽毛球'],
        'user': ['user'],
        'content': '<p>数据库查询出来的带有标签的数据</p>',
        'defaultText': ''
    }
    return render(request, "index.html",context=content)
def book(request):
    return render(request, "base.html")
def clothes(request):
    return  render(request,"clothes.html")