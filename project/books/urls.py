from django.conf.urls import patterns, url

urlpatterns = patterns('books.views',
        url(r'^data/$', 'data')
)
