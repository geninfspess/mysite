# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejc', '0018_auto_20170403_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='servo',
            name='celular2',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='servo',
            name='email2',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
    ]