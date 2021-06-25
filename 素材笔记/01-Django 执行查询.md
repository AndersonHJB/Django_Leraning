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
```

