# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 01:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20161002_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 2, 10, 23, 49, 651747), verbose_name='date published'),
        ),
    ]