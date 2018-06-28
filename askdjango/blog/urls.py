#blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]
'''
첫번째 값은 blog이후에 값이 X
'''