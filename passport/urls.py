from django.conf.urls import url, include
from django.contrib import admin
from passport.views import *

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^login/login/', logins, name="logins"),
    url(r'^login_out/', login_out, name="login_out"),
]
