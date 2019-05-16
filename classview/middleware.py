# 中间件的固定写法，类似于装饰器
from django.http import HttpResponse


def my_middleware(view_func):

    # 中间件注册时调用
    print("init 被调用")

    def middleware(request):
        #请求之前被调用
        forbiden = ["192.168.129.1"]
        if request.META['REMOTE_ADDR'] not in forbiden:
            print(request.META['REMOTE_ADDR'])
        # 进入视图函数执行，并获取到视图函数返回的响应对象
            response = view_func(request)
        # 响应完成后执行
        else:
            response = HttpResponse("禁止访问")
        print("after request 被调用")

        return response

    return middleware


def my_middleware2(view_func):

    # 中间件注册时调用
    print("init2 被调用")

    def middleware(request):
        #请求之前被调用
        print("before request2 被调用")
        # 进入视图函数执行，并获取到视图函数返回的响应对象
        response = view_func(request)
        # 响应完成后执行
        print("after request2 被调用")

        return response

    return middleware
