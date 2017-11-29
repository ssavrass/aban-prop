# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-21 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20171120_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='title',
        ),
        migrations.AddField(
            model_name='properties',
            name='city',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='properties',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='properties',
            name='housenumber',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='properties',
            name='levels',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='properties',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='properties',
            name='street',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='properties',
            name='type',
            field=models.TextField(default=''),
        ),
    ]
