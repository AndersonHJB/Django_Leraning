# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 2:50 下午
# @Author  : AI悦创
# @FileName: urls.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
# 课程方法
# from django.conf.urls import url
# from jobs import views
#
# urlpatterns = [
# 	# 职位列表
# 	url(r"^joblist/", views.joblist, name="joblist")
# ]
# 比较好理解的方法
from django.urls import path
from . import views

urlpatterns = [
	path('joblist/', views.joblist, name='joblist'),
]
