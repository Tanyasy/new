from django.db import models
import time

# 自定义管理类
class BookInfoManage(models.Manager):
    def all(self):
        return super().filter(is_delete=False)

    def overthree(self):
        return super().filter(id__gt=3)


# Create your models here.
class BookInfo(models.Model):

    # 创建管理类对象
    # 创建对象后，books将替代objects成为管理
    books = BookInfoManage()

    btitle = models.CharField(max_length=20, verbose_name="书籍名称")
    bpub_date = models.DateField(verbose_name="出版日期")
    bread = models.IntegerField(default=0, verbose_name="阅读量")
    bcomment = models.IntegerField(default=0, verbose_name="评论量")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")
    image = models.ImageField(upload_to="pid", verbose_name="图片", null=True)

    class Meta:
        # 元类，指明数据库的表的名称，如果没有指明默认使用：子应用名小写_模型类名小写做为表名
        db_table = "tb_books"
        verbose_name = "图书"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.btitle

    def pub_date(self):
        return self.bpub_date.strftime('%Y-%m-%d')

    pub_date.short_description = "发布日期"
    pub_date.admin_order_field = "bpub_date"


class HeroInfo(models.Model):
    GENDER_CHOICE = (
        (0, "男"),
        (1, "女")
    )
    hname = models.CharField(max_length=20, verbose_name="英雄名称")
    hgender = models.SmallIntegerField(choices=GENDER_CHOICE, verbose_name="性别")
    hcomment = models.CharField(max_length=200, null=True, verbose_name="描述信息")
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name="图书")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    class Meta:
        # 元类，指明数据库的表的名称，如果没有指明默认使用：子应用名小写_模型类名小写做为表名
        db_table = "tb_heros"
        verbose_name = "英雄"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname

    def read(self):
        return self.hbook.bread

    read.short_description = "图书阅读量"