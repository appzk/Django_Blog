# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-07 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_auto_20190807_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommentmodel',
            name='to_code',
            field=models.UUIDField(blank=True, null=True, verbose_name='对方用户uid'),
        ),
    ]
