# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('responsable', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('localizacion', models.CharField(max_length=20)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('activo', models.IntegerField()),
            ],
        ),
    ]
