# -*- coding: utf-8 -*-
from django.conf.urls import re_path, include

__all__ = [
    'app_name', 'urlpatterns',
]

app_name = 'restapi'
urlpatterns = [
    re_path(r'^minis/', include('minis.urls.restapi')),
]
