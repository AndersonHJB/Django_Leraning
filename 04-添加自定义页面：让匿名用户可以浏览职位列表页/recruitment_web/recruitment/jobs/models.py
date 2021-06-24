from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

JobTypes = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
    (3, "设计类"),
]

Cities = [
    (0, "北京"),
    (1, "上海"),
    (2, "深圳"),
]

# 每个字段都可以设置默认值，使用 default 就好。文本的值你也可以设置成默认的文本
class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别")
    job_name = models.CharField(max_length=250, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name="工作地点")
    job_reponsibility = models.TextField(max_length=1024, verbose_name="职位职责")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求")
    creator = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL, default=User)
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改时间", default=datetime.now)

    def __str__(self):
        return self.job_name
# # 每个字段都可以设置默认值，使用 default 就好。文本的值你也可以设置成默认的文本
# class Job(models.Model):
#     job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别", default=JobTypes[0])
#     job_name = models.CharField(max_length=250, blank=False, verbose_name="职位名称", default="填写职位名称")
#     job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name="工作地点", default=Cities[0])
#     job_reponsibility = models.TextField(max_length=1024, verbose_name="职位职责", default="这里你可以填写你的职位职责")
#     job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求", default="这里可以写你招聘的职位要求")
#     creator = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL, default=User)
#     created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
#     modified_date = models.DateTimeField(verbose_name="修改时间", default=datetime.now)
