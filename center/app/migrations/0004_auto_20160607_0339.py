# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_costperday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costperday',
            name='create_time',
            field=models.DateField(default=None, null=True),
        ),
    ]
