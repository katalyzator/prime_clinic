# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import Slider


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

    class Meta:
        model = Slider


admin.site.register(Slider, SliderAdmin)
