#dojo/urls.py
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$',views.hello),
    url(r'^post_list1/$', views.post_list1),
    url(r'^post_list2/$', views.post_list2),
    url(r'^post_list3/$', views.post_list3),
    url(r'^excel/$', views.excel_download),
]