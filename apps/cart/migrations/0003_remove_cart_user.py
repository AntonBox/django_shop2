# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-20 15:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]