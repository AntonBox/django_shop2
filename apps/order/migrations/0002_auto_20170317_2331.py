# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-17 23:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_squashed_0005_auto_20170315_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='token',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
