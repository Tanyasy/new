from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    content1 = {
        "my_str": "蔡徐坤",
        "my_int":23,
        "my_list": ["唱", "跳", "rap", "篮球"],
        "my_dict": {"name":"hander","team":"rocket"},
        "my_date": date(1990,1,1),
        "html_str": "<h1>首页</h1>"
    }

    return render(request, "index.html", context=content1)


def jinja(request):
    content1 = {
        "my_str": "蔡徐坤",
        "my_int":23,
        "my_list": ["唱", "跳", "rap", "篮球"],
        "my_dict": {"name":"hander","team":"rocket"},
        "my_date": date(1990,1,1),
        "html_str": "<h1>首页</h1>"
    }

    return render(request, "jinja2.html", context=content1)


def father(request):

    return render(request, "father.html")


def children(request):

    return render(request, "children.html")