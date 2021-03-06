"""wxgraduation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from show import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'index', views.index),  # 新增url解析规则，什么网址对应什么函数
    path(r'', views.index),
    path(r'chart', views.chart),
    path(r'demo', views.demo),
    path(r'datatable', views.datatable),
    path(r'refreshMovieInfo', views.refresh_movie_info),  # 重新爬取电影信息
]
