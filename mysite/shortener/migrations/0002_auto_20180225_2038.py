# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-25 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='short_link',
            field=models.CharField(max_length=32),
        ),
    ]
