#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    author:haiyang.xing
    datetime:2022/7/27 14:07
"""
from django.urls import re_path, path

from chat import consumers
websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/(?P<user_name>\w+)/$", consumers.ChatConsumer),
    path("ws/push/<room_name>", consumers.PushMessage),
]