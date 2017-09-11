# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('question_count', models.IntegerField(default=0)),
                ('penalty', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField()),
                ('duration', models.DateTimeField()),
                ('total_score', models.IntegerField(default=0)),
            ],
        ),
    ]
