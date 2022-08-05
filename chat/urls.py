#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    author:haiyang.xing
    datetime:2022/7/27 11:42
"""
from django.urls import path

from chat import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/<str:user_name>/', views.room, name='room'),
]