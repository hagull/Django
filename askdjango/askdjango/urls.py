"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import RedirectView
def root(request):
    return redirect('blog:post_list')

urlpatterns = [
    #url(r'^$', root, name = 'root'),
    # 함수 지정을 따로 안하고 lambda 함수로도 지정이 가능
    url(r'^$', lambda r: redirect('blog:post_list'), name = 'root'),
    #람다 함수는 함수의 축약형 ex) g = lambda x,y : x * y // g(2,3) = 6 이런식으로 이것도 파이썬 문법
    #url(r'^$', RedirectView.as_view(pattern_name= 'blog:post_list')), 로도 지정가능
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace= 'blog')),
    url(r'^dojo/', include("dojo.urls", namespace= "dojo")),
    url(r'^accounts/', include("accounts.urls", namespace="accounts")),
    url(r'^shop/', include('shop.urls', namespace="shop")),
]
# 실 서비스 에서는 setting.py의 DEBUG 옵션은 False 로 둔다 TRUE는 개발옵션을 킨다는 뜻
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    #해당 html에 body태그가 있어야 표현가능 바디태그가 기준이된다
    #url 패턴즈에 추가한다