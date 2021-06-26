from django.contrib import admin
from blog.models import Blog, Author, Entry
# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
