# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20171003_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='contests',
            name='c_type',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='questions',
            name='image_url',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='options',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='problem_type',
            field=models.BooleanField(default=True),
        ),
    ]