# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childcare_app', '0004_auto_20161105_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='on_site',
            field=models.BooleanField(default=False),
        ),
    ]
