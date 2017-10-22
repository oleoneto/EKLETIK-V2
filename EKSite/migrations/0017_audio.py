# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-22 06:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EKSite', '0016_auto_20171020_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(max_length=60, upload_to='uploads/audios/')),
                ('number', models.IntegerField(blank=True)),
                ('title', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('composer', models.CharField(blank=True, max_length=50)),
                ('genre', models.CharField(blank=True, max_length=15)),
                ('publishedDate', models.DateField(blank=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EKSite.PortfolioProject')),
            ],
        ),
    ]
