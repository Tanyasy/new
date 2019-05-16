import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
"""
get请求：向后端查询获取数据 参数在url路径后通过?携带
post请求：向后端提交数据 请求体携带参数


需求：研究利用http协议向后端发送请求携带参数的几种方式:

1.路由url的路径传递参数
eg: http://127.0.0.1:8000/weather/  通过`正则表达式`提取

2.查询字符串传递参数
eg: http://127.0.0.1:8000/user?name=curry&like=basketball 
目的：提取get请求问号后面携带的键值对参数

3.请求体(body)传递参数
参数在请求体中
分类：
    1> form表单数据
    2> 非表单  ajax请求json格式数据，xml，text

4.请求头(header)传递参数

"""


def index(request):
    return HttpResponse("研究利用http协议向后端发生请求携带参数的几种方式")


def weather(request, city, year):
    '''1.路由URL的路径传递参数'''

    # 参数未命名：参数有顺序要求
    #　参数命名：顺序随意
    return HttpResponse("路由url的路径传递参数　城市：%s 年份：%s" % (city, year))


def query_user(request):

    # 1.利用request.GET属性qu提取查询字符串参数
    param_dict = request.GET
    print(request.GET)
    print(type(request.GET))

    # name = param_dict["name"]
    name = param_dict.get("name", "哈哈")

    return HttpResponse("查询字符串传递参数：%s" % name)


def body_form(request):
    '''3.请求体方式传参'''
    param_dict = request.POST

    print(request.POST)
    print(type(request.POST))

    name = param_dict.get("name", "")
    age = param_dict.get("age", "")
    return HttpResponse("请求体传递参数--form表单格式: %s %s" % (name, age))


def body_notform(request):
    '''4.求体传递参数--非表单格式数据 json xml text'''
    # 接受二进制数据
    data = request.body
    # 将数据转换成json格式字符串
    json_data = data.decode()
    print(type(json_data))
    # 将json格式字符串转成python字典
    my_dict = json.loads(json_data)

    return HttpResponse("请求体传递参数---非表单格式数据： %s" % my_dict)


def header(request):
    '''5.请求头传递参数'''
    # 1.通过request.META属性提取请求头携带的参数[字典]
    my_dict = request.META

    content_type = my_dict.get("CONTENT_TYPE", "")

    return HttpResponse("请求头传递参数：%s" % content_type)


def other(request):
    '''6.httprequest请求对象其他常用属性'''
    method = request.method

    print(method)

    user = request.user

    print(user)

    path = request.path

    print(path)

    encoding = request.encoding

    print(encoding)

    return HttpResponse("6.HTTPRequest请求对象其他常用属性")