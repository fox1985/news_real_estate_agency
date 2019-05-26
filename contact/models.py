# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Provele(models.Model):
    img = models.ImageField(upload_to='prov_img', verbose_name='Профиль агента', blank=True)
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    prov_email = models.EmailField(verbose_name='Почта')






class Emailcontact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField()