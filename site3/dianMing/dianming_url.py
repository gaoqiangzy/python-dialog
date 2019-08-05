from django.conf.urls import url
import  dianMing.views as dianMing_view
urlpatterns = [
    url('^$',dianMing_view.index)
]