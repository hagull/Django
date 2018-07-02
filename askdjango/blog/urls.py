#blog/urls.py
from django.conf.urls import include, url
from . import views
from  django.conf import settings
urlpatterns = [
    url(r'^$', views.post_list),

]

'''
첫번째 값은 blog이후에 값이 X
'''