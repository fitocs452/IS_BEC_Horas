# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_activity_time_worth1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='time_worth1',
        ),
        migrations.AlterField(
            model_name='activity',
            name='time_worth',
            field=models.CharField(max_length=200),
        ),
    ]