# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
    ]
