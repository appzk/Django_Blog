# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-09 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20190808_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photodetailmodel',
            options={'verbose_name_plural': '相片集合'},
        ),
        migrations.AlterModelOptions(
            name='photomodel',
            options={'verbose_name_plural': '相册'},
        ),
        migrations.AlterField(
            model_name='photodetailmodel',
            name='img',
            field=models.ImageField(upload_to='photo_detail', verbose_name='相片'),
        ),
        migrations.AlterField(
            model_name='photomodel',
            name='img',
            field=models.ImageField(upload_to='photo', verbose_name='封面图片'),
        ),
    ]
