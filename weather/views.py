from django.http import HttpResponse
from django.shortcuts import render


def getinfo(request, time, addr):
    # print(f"接受的时间为：{time}，地点为：{addr}")
    return HttpResponse(f"接受的时间为：{time}，地点为：{addr}")
