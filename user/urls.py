from django.conf.urls import url
from user import views

urlpatterns = [
    # 为index配置路由
    url(r'^index/$', views.index, name="index"),

]