"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django.shortcuts import HttpResponse, render,redirect

from from01 import UploadFileForm
from settings import BASE_DIR

# def cha(request):
#     return render(request,'chawancheng.html')
#
# def cun(request):
#     for request.method == 'get':
#     return render(request,'cunwancheng.html')

def load(request):
    # return HttpResponse('成功')
    if request.method == 'GET':
        return render(request, 'es.html')
    # else:
    #     if request.method == 'POST':
    #         return redirect('cunwancheng.html')

def upload_file(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        with open(os.path.join(BASE_DIR, 'static', 'pic', file_obj.name), 'wb') as f:
            print(file_obj, type(file_obj))
            for chunk in file_obj.chunks():
                f.write(chunk)
        return HttpResponse('OK')


urlpatterns = [
    path('load/', load),
    path('upload/', upload_file),
]
