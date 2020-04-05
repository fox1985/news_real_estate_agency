# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    email = models.EmailField()
    nomer_id = models.CharField(max_length=100)
    body = models.TextField()

    def __unicode__(self):
        return self.mame

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'