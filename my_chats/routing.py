#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    author:haiyang.xing
    datetime:2022/7/27 14:07
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_chats.settings')

from channels.auth import AuthMiddlewareStack
import chat.routing
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.sessions import SessionMiddlewareStack

application = ProtocolTypeRouter({

    "websocket": AllowedHostsOriginValidator(
        SessionMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    ),

})