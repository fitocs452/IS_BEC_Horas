# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='aa', max_length=200),
        ),
    ]
