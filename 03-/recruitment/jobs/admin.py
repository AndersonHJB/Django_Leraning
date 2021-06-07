from django.contrib import admin
from jobs.models import Job


# Register your models here.
# 方法二：
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
	# fields = ('url', 'title', 'content')
	list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')  # 在 ModelAdmin 中有特定含义的属性，当我们配置这个列表之后，列表页就会把这些字段展现出来。
	
	exclude = ('creator', 'created_date', 'modified_date')  # 隐藏不想显示的
	
	# fields = ('created_date', 'creator', 'modified_date')  # 选择想要显示的，而且其中元组的顺序也就是后台显示的顺序
	
	# 有个问题，我们把这些字段进行隐藏了，那系统里面是没有这些属性的，所以这个时候我们可以利用 JobAdmin ，利用 ModelAdmin 的一个方法
	# save_model 它是 ModelAdmin 这个父类里面的一个定以的方法
	# 这个方法可以在我们保存一个模型之前去做一个操作，比如说：
	# 我们把职位的创建人设置成当前的用户 obj.creator = request.user  这样就可以把当前登录的用户设置成这个 model 的创建人。「职位的创建人」
	def save_model(self, request, obj, form, change):
		obj.creator = request.user
		# 这里我们调用一下父类的方法：
		super().save_model(request, obj, form, change)  # 来保存我们的对象，这个 save_model 会被自动调用

# 把 JobAdmin 注册到站点里面
# admin.site.register(Job, JobAdmin)
# admin.site.register(Job)
