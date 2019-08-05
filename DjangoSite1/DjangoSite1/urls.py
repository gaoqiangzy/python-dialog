"""DjangoSite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

"""
定义视图函数
1.Django中，所有视图函数第一个参数必须预留request
2.django中，所有的视图函数必须返回一个HttpResponse对象
"""
def hello(request):
    return HttpResponse("hello world")



#路由列表
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),#将url地址与视图函数
]
