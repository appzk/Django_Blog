# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-01 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_growth_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.DateField(blank=True, null=True, verbose_name='年龄'),
        ),
    ]
