# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class Realtor(models.Model):
  name = models.CharField(max_length=200)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  is_mvp = models.BooleanField(default=False)
  hire_date = models.DateTimeField(default=datetime.now, blank=True)

  class Meta:
    verbose_name = 'риэлтор'
    verbose_name_plural = 'риэлторы'


  def __unicode__(self):
    return self.name

