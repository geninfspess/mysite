# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejc', '0010_remove_inscricao_padrinho'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=70)),
                ('assunto', models.CharField(max_length=200)),
                ('mensagem', models.TextField()),
            ],
        ),
    ]