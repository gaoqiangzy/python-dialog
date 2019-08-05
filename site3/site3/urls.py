"""site3 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf  将主路由和子路由绑定
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from site3 import main_view
from site3.main_view import test

urlpatterns = [
    #将url地址通过正则匹配到对应的视图函数
    url(r'^$', main_view.index),#配置首页路由
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', main_view.index),
    url(r'^rvs/$', main_view.rvs),
    url(r'^test/(?P<bid>\d+)$', test),
    #从url截取有用字符串，将有用数据用（）包住，并自动将数据传递到视图函数
    #位置参数
    # url(r'^detail/([a-z]+)/(\d+).html', main_view.detail),
    #命名参数  P--->parameter
    url(r'^detail/(?P<category>[a-z]+)/(?P<id>\d+).html$', main_view.detail),

    # ''' 图书模块 '''
    url(r'^book/', include('book.book_url',namespace="book")),

    #电影模块
    url(r'^movie/',include('movie.movie_url',namespace="movie")),

    # '''点名模块'''run
    url(r'^dianMing/',include('dianMing.dianming_url')),

    #音乐模块
    url(r'^music/',include('music.music_url')),
]
