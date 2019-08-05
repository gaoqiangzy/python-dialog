from django.conf.urls import url

from music.views import index, xiangqing
import music.views as mv
urlpatterns =[
    url('^$',index),
    url('^xiangqing$',mv.xiangqing,name="xiangqing"),
]