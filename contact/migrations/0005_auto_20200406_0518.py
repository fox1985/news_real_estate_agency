# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-04-06 05:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20200404_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='body',
            new_name='message',
        ),
    ]