# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0004_auto_20170603_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='router',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]