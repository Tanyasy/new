from jinja2 import Environment


# django中使用jinja2模板引擎的环境
def environment(**options):

    env = Environment(**options)

    env.filters["do_reverse"] = do_reverse

    return env


def do_reverse(list):
    list.reverse()

    return list