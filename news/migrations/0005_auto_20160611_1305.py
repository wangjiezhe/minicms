# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20160611_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='intro',
            field=models.TextField(blank=True, default='', verbose_name='栏目简介'),
        ),
    ]