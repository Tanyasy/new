# 需求：自定义列表反转的过滤器
# 1.导入template模块
from django import template


# 2.创建一个注册对象
register = template.Library()


# 3.自定义python中的函数完成业务
@register.filter
def do_listreverse(list):

    list.reverse()

    result = ''

    for i in list:
        result += i+"\t"

    return result


@register.filter
def headupper(str):

    str = str[0].upper() + str[1:]

    return str