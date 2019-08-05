from django.conf.urls import url

from movie.views import index, detail

urlpatterns = [
    url("^$",index,name="index"),
    url('^(?P<mid>\d+)$',detail)
]