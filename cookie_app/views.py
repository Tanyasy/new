from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):

    # 需求：登录成功借助响应对象设置cookie信息
    response = HttpResponse(content="登录成功，设置cookie")

    response.set_cookie("name", "laowang", max_age=3600)
    response.set_cookie("is_login", "True", max_age=3600)

    return response


def index(request):

    # 获取浏览器返给客户端的cookie
    param_dict = request.COOKIES
    print(type(param_dict))
    name = param_dict.get("name", "")
    is_login = param_dict.get("is_login", "")

    return HttpResponse("首页： %s  %s" % (name, is_login))
