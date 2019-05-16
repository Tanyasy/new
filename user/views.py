from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index(request):
    # 反向解析
    path = reverse("index")
    return HttpResponse(f"hello world{path}")
