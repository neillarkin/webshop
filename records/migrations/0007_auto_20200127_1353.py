# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-27 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_auto_20200117_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
