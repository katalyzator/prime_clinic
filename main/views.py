# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from main.models import Slider


def index_view(request):
    sliders = Slider.objects.all()
    context = {
        "sliders": sliders
    }
    template = 'main/index.html'

    return render(request, template, context)
