# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180509_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='o_status',
            field=models.IntegerField(default=0),
        ),
    ]
