# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-05 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190801_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='classify',
            name='code',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='类型编码'),
        ),
        migrations.AddField(
            model_name='tag',
            name='code',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='标签编码'),
        ),
    ]
