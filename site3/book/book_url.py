'''
    子路由：
        无论主路由还是子路由，都是将url地址和视图函数绑定在一起
'''
from django.conf.urls import url
from book.views import index, detail

urlpatterns = [
    url('^$',index,name="index"),#name：视图的名字，根据name，可以反向得出视图的url地址
    url('^(?P<bid>\d+)$',detail,name="书详情页"),
]