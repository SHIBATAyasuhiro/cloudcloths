# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 21:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 12, 6, 48, 12, 131696), verbose_name='date published'),
        ),
    ]
