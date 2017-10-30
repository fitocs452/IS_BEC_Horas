# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.CharField(max_length=200, unique=True)),
                ('Name', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('major', models.CharField(max_length=200)),
                ('cuota', models.IntegerField(default=50)),
            ],
        ),
    ]
