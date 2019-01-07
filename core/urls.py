# -*- coding: utf-8 -*-
from django.conf.urls import url

from core.views import get_popular_themes

urlpatterns = [
     url(r'^themes/$', get_popular_themes, name='get_popular_themes'),
]