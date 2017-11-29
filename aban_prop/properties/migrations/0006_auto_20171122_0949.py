# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-22 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20171121_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='properties',
            old_name='city',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='properties',
            name='housenumber',
        ),
        migrations.RemoveField(
            model_name='properties',
            name='street',
        ),
    ]
