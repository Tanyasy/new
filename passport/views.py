from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":

        user = request.POST.get("user", None)
        passwd = request.POST.get("password", None)

        if not all([user, passwd]):
            print("用户信息不全，请重新输入")
            # return redirect(reverse("login"))
        else:
            if user == "zhangsan" and passwd == "123":
                return HttpResponse(f"登录成功，欢迎{user}")
            else:
                print("密码错误")
                # return redirect('/login.html')


def logins(request):
    return HttpResponse("登录成功，欢迎")



def login_out(request):
    path = reverse("passport:login_out")
    return HttpResponse(f"退出成功,{path}")
