# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-04 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_preview',
            field=models.CharField(default='Exciting News', max_length=400),
            preserve_default=False,
        ),
    ]
