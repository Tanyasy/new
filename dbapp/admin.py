from django.contrib import admin
from dbapp.models import *


class HeroInfoStackInline(admin.TabularInline):
    # 要编辑的对象
    model = HeroInfo
    # 附加编辑的数量
    extra = 1


# 定义管理类
class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 5
    # 显示项目
    list_display = ["btitle", "pub_date", "bread", "bcomment", "image"]
    # 过滤项目
    list_filter = ["bpub_date"]
    # 搜索框
    search_fields = ["btitle"]
    # 分组显示
    fieldsets = (
        ('必填', {'fields': ("btitle", "bpub_date")}),
        ('选填', {
            'fields': ("bread", "bcomment", "image"),
            'classes':("collapse",)
                }),
    )
    # 关联对象
    inlines = [HeroInfoStackInline]


class HeroInfoAdmin(admin.ModelAdmin):
    # 设置每页显示数据的个数
    list_per_page = 5
    # 设置动作按钮是否在底部显示
    # actions_on_bottom = True
    list_display = ["hname", "hbook", "read"]
    # 过滤项目
    list_filter = ["hbook"]
    # 搜索框
    search_fields = ["hname"]
    # 分组显示
    fieldsets = (
        ('必填', {'fields': ("hname", "hbook")}),
        ('选填', {'fields': ("read",)}),
    )



# 调整站点信息
admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'

# 模型类注册
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)