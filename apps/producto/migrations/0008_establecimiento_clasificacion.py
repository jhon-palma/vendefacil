# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-17 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_auto_20170311_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='establecimiento',
            name='clasificacion',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
