"""test03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from request import views


urlpatterns = [

    # 为passport配置路由
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    # 为query_user配置路由
    url(r'^query_user/$', views.query_user),

    url(r'^body_form/$', views.body_form),

    url(r'^body_notform/$', views.body_notform),
    url(r'^header/$', views.header),
    url(r'^other/$', views.other),
]


