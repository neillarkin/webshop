# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-17 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('records', '0005_auto_20200117_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='genre',
        ),
        migrations.AddField(
            model_name='record',
            name='genres',
            field=models.ManyToManyField(to='genres.Genre'),
        ),
    ]
