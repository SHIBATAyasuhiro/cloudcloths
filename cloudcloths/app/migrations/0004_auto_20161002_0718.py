# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 22:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160912_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.CharField(default='no-brand', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 2, 7, 18, 46, 731713), verbose_name='date published'),
        ),
    ]
