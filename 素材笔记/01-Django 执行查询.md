# 01-Django 执行查询

## 1. 新建一个项目用来测试

为了更好的理解，我创建一个相对应的 Django 项目来理解这篇文章所涉及的知识点。

### 1.1 新建虚拟环境

```python
python3 -m venv djangoenv
```

### 1.2 Mac 进入虚拟环境

```python
source djangoenv/bin/activate
```

### 1.3 安装 Django 库

```python
pip install django
```

### 1.4 创建一个 Django 项目

```python
django-admin startproject Webblog
```

### 1.5 启动服务

```python
python manage.py runserver
```

### 1.6 创建 blog app

```python
python manage.py startapp blog
```

## 2. 写入如下代码 models.py

```python
from django.db import models


# Create your models here.
class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()
	
	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	
	def __str__(self):
		return self.name


class Entry(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	headline = models.CharField(max_length=255)
	body_text = models.TextField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	authors = models.ManyToManyField(Author)
	number_of_comments = models.IntegerField()
	number_of_pingbacks = models.IntegerField()
	rating = models.IntegerField()
	
	def __str__(self):
		return self.headline
```

### 2.1 数据库迁移

```python
python manage.py migrate
```

### 2.2 创建超级管理员

```python
(djangoenv) ➜  Webblog git:(main) ✗ python manage.py createsuperuser
Username (leave blank to use 'apple'): example_uesr
Email address: example@aiyc.top
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

- 账号：example_user
- 密码：123123

### 2.3 注册 blog

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'blog'
]
```

### 2.4 注册到 admin

```python
from django.contrib import admin
from blog.models import Blog, Author, Entry
# Register your models here.
admin.site.register(Blog)
```

### 2.5 运行数据看迁移

```python
 python manage.py makemigrations
```

