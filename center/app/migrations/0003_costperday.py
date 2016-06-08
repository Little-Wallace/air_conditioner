# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160602_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostPerDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.FloatField(default=0.0, max_length=8, null=True)),
                ('day_cost', models.FloatField(default=0.0, max_length=8, null=True)),
                ('create_time', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'db_table': 'cost_per_day',
            },
        ),
    ]