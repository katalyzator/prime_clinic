# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode


class Slider(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/slider', verbose_name='Картинка')

    class Meta:
        verbose_name_plural = 'Слайдер на главной странице'
        verbose_name = 'слайд'

    def __unicode__(self):
        return smart_unicode(self.title)
