from django.conf.urls import url
from weather import views

urlpatterns = [
    # 为index配置路由
    url(r'^(?P<addr>[a-zA-Z]+)/(?P<time>\d{4})/$', views.getinfo, name="getinfo"),

]