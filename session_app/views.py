from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    # 接受request，设置session
    request.session["name"] = "laowang"
    request.session["id"] = "001"
    request.session.set_expiry(3600)
    return HttpResponse("session设置成功")


def check(request):

    dict1 = request.session
    name = dict1.get("name")
    id = dict1.get("id", "")
    # print("结果",hasattr(dict1, 'name'))
    if name:
        # name = dict1["name"]
        if name == "laowang":
            return HttpResponse(f"欢迎{name}")
        else:
            return HttpResponse(f"欢迎{name}")
    else:
        return HttpResponse("登录失败")


def login_out(request):
    # 删除session
    # del request.session["name"]
    # 删除当前所有用户的session的值，记录任然存在
    request.session.clear()
    # 删除当前用户的整条记录，会去掉客户端的cookie
    request.session.flush()
    return HttpResponse("退出成功")