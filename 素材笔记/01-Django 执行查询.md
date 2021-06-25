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

