# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-07-07 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenmeurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='shortenmeurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='shortenmeurl',
            name='url',
            field=models.CharField(max_length=220),
        ),
    ]
