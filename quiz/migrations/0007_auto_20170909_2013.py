# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 20:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0006_auto_20170909_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('wrong', models.IntegerField(default=0)),
            ],
        ),
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
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.CharField(max_length=50)),
                ('problem_statement', models.CharField(max_length=2000)),
                ('answer', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'')),
                ('announcement', models.CharField(max_length=2000)),
                ('max_score', models.IntegerField(default=0)),
                ('contest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Contests')),
            ],
        ),
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.IntegerField(default=0)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Contests')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='attempts',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Contests'),
        ),
        migrations.AddField(
            model_name='attempts',
            name='u_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
