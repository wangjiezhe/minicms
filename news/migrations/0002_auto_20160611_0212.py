# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 02:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='put_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 11, 2, 12, 5, 45927, tzinfo=utc), verbose_name='发布时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
    ]
