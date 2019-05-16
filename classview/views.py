from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_decorator(func):

    def warpper(request, *args, **kwargs):
        print("装饰器调用了")
        return func(request, *args, **kwargs)

    return warpper


# 普通的判读方式
def index(request):
    if request.method == "GET":
        return HttpResponse("以get方式连接")
    elif request.method == "POST":
        return HttpResponse("以post方式连接")


#　用类视图实现判断请求方式
# @method_decorator(my_decorator, "post")  # 只装饰里面的post方法
@method_decorator(my_decorator, "dispatch")  # 装饰里面的所有方法
class IndexClassView(View):

    def get(self, request):
        return HttpResponse("以get方式连接")

    def post(self, request):
        return HttpResponse("以post方式连接")