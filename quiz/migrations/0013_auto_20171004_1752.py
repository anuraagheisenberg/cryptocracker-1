# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20171004_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contests',
            name='penalty',
            field=models.BooleanField(default=0),
        ),
    ]
