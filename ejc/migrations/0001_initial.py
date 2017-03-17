# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=9)),
                ('celular', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]