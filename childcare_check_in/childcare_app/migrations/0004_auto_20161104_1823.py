# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childcare_app', '0003_auto_20161103_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='check_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='child',
            name='check_out',
            field=models.DateTimeField(),
        ),
    ]
