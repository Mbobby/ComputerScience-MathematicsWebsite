# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-10 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170310_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
