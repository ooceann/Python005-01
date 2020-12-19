# -*- coding: utf-8 -*-
# @FileName: urls.py
# @Time    : 2020/12/18 11:30 下午
# @Author  : zhan
from django.urls import path, re_path, register_converter

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='index'),
    # path('index', views.index, name='index')
]
