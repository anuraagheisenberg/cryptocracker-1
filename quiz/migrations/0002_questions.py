# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 22:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=50)),
                ('problem_statement', models.CharField(max_length=2000)),
                ('answer', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'')),
                ('announcement', models.CharField(max_length=2000)),
                ('max_score', models.IntegerField(default=0)),
                ('contest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
