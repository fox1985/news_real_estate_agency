# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True)
    phone = models.CharField(max_length=100, verbose_name=u'Телефон')
    email = models.EmailField(max_length=100, verbose_name='Email')


    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


