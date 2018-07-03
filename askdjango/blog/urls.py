#blog/urls.py
from django.conf.urls import include, url
from . import views
from  django.conf import settings
urlpatterns = [
    url(r'^$', views.post_list),
    url('^(?P<id>\d+)/$', views.post_detail),
]

'''
첫번째 값은 blog이후에 값이 X
'''