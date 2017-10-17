# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-14 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EKSite', '0014_auto_20170910_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('origin', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='FeaturedHeader',
        ),
        migrations.AlterModelOptions(
            name='doc',
            options={'verbose_name_plural': 'Documentation & Blog'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'Team Members'},
        ),
        migrations.AlterModelOptions(
            name='portfolioproject',
            options={'verbose_name_plural': 'Portfolio Projects'},
        ),
        migrations.AlterField(
            model_name='doc',
            name='programmingLanguage',
            field=models.CharField(choices=[('code', 'Coding'), ('news', 'Notícias'), ('exp', 'Experimentos'), ('rb', 'Ruby'), ('py', 'Python'), ('sh', 'ShellScript'), ('md', 'Markdown'), ('c', 'C'), ('cpp', 'C++'), ('csp', 'C#'), ('java', 'Java'), ('ru', 'Rust'), ('swift', 'Swift'), ('m', 'Objective-C'), ('html', 'HTML'), ('css', 'CSS'), ('js', 'JavaScript'), ('web', 'HTML, CSS, JavaScript'), ('node', 'NodeJS'), ('dj', 'Django'), ('rails', 'Ruby on Rails'), ('as', 'Apple Script'), ('r', 'R')], default='py', max_length=5),
        ),
    ]