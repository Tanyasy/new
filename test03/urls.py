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
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 为index配置路由
    url(r'^user/', include('user.urls')),
    # 为passport配置路由
    url(r'^passport/', include('passport.urls', namespace="passport")),
    # 为weather配置路由
    url(r'^weather/', include('weather.urls', namespace="weather")),
    # 为request配置路由
    url(r'^request/', include('request.urls', namespace="request")),
    # 为response_app配置路由
    url(r'^response/', include('response_app.urls', namespace="response")),
    # 为cookie_app配置路由
    url(r'^cookie/', include('cookie_app.urls', namespace="cookie")),
    # 为session_app配置路由
    url(r'^session/', include('session_app.urls', namespace="session")),
    # 为classview配置路由
    url(r'^classview/', include('classview.urls', namespace="classview")),
    # 为template_app配置路由
    url(r'^template/', include('template_app.urls', namespace="template")),
]
