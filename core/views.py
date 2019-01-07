# -*- coding: utf-8 -*-
from django.shortcuts import render

from core.models import Theme


def get_popular_themes(request):

    themes_q = Theme.objects.all().prefetch_related('video_set__comment_set', 'video_set__thumb_set')

    themes = sorted(themes_q, key = lambda x: x.score()) 
    context = {'themes': themes}
    return render(request, 'themes/get_popular_themes.html', context)

def index(request):

    return render(request, 'index.html', locals())