# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from jobs.models import Job
from jobs.models import Cities, JobTypes  # 因为这两个数据是 choice 来选择的，数据提取的时候只提取出了数字。


def joblist(request):
	# https://docs.djangoproject.com/zh-hans/3.2/ref/models/querysets/#order-by
	job_list = Job.objects.order_by('job_type')  # 从数据库获取，并且以 job_type 排序
	template = loader.get_template('joblist.html')  # 加载模版
	"""定义上下文——map"""
	context = {'job_list': job_list}
	for job in job_list:
		"""因为，我们需要显示的数据是：工作地点、工作类型，但是我们的这两个数据都是由 choices 来实现选择的。所以，job.xxx 都是返回下标的「也就是数字」"""
		job.city_name = Cities[job.job_city][1]  # 工作地点
		job.job_type = JobTypes[job.job_type][1]  # 职位类别
	return HttpResponse(template.render(context))
