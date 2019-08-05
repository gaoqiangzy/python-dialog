from django.conf.urls import url
import  book.views as book_view
urlpatterns =   [
    url('^$',book_view.index)
]
