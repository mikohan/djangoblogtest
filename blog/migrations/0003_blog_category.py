# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-06-06 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]