from django.shortcuts import render
from django.http import HttpResponse  # 从 django 的 http 模块引入 HttpResponse 函数


# from 某某模块的某某子模块 import 某个函数

def index(request):
	# 定义一个 index 函数处理主页的访问请求 Request 包含了用户浏览器传来的 HTTP 请求内容
	return HttpResponse("欢迎来到 AI悦创博客！")  # 用 HttpResponse 函数直接返回一段文字给用户


def blog_detail(request, blog_id):
	return HttpResponse("这是第「{}」篇博客".format(blog_id))


def blog_sum(request, blog_id1, blog_id2):
	# return HttpResponse("Result:{blog_id1} + {blog_id2} = {result_sum}".format(blog_id1=blog_id1, blog_id2=blog_id2, result_sum=blog_id1 + blog_id2))
	return HttpResponse(f"Result:{blog_id1} + {blog_id2} = {blog_id1 + blog_id2}")
