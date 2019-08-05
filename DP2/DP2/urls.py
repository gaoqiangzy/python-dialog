"""DP2 URL Configuration

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
from DP2 import views
def gaoqiang(request):
    username = request.GET.get("username")
    return HttpResponse(f"hello {username}")
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^gaoqiang/', views.gaoqiang), #args1 路径访问名  args2 路径名对应函数
    url(r'^gaoqiang/$',gaoqiang),
]
