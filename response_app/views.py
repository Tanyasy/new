from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def redirect_response(request):
    '''

    重定向响应对象
    :param request:
    :return:
    '''

    # url = reverse('index')

    return redirect('/user/index/')


def json_response(request):

    my_dict = {
        "name": "durant"
    }

    return JsonResponse(my_dict)


def index(request):
    # 构建响应对象
    response = HttpResponse()
    response.content = "我是响应内容--操作对象"

    response.status_code = 200
    response['Content-Type'] = "application/json"

    # response = HttpResponse(content="我也是响应内容",  status=200)
    return response