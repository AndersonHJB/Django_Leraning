from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.index, name='index'),
	# path(route, view)
	# path(route, view, name="'index'")
	path('<int:blog_id>', views.blog_detail, name='blog_detail'),
	path('<int:blog_id1>/<int:blog_id2>', views.blog_sum, name='blog_sum')
]

# 单词 route
"""
n. 路线，航线；道路，公路；（交通工具的）固定路线；巡访；途径，渠道；（北美）递送路线；用于美国干线公路号码前
v. 按特定路线发送，为……规定路线
"""
