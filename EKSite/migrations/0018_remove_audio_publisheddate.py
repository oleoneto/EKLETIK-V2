# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-22 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EKSite', '0017_audio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='publishedDate',
        ),
    ]