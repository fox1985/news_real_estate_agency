# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
    mame = models.CharField(max_length=100)
    email = models.EmailField()
    nomer_id = models.CharField(max_length=100)
    body = models.TextField()