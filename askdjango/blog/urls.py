#blog/urls.py
from django.conf.urls import include, url
from . import views
from  django.conf import settings
urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name= 'post_detail'),
    #name 을 지정하게 되면 -> post_list에 이어서 설명
]

'''
첫번째 값은 blog이후에 값이 X
'''