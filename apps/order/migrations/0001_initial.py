# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 11:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cart', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='cart.Cart')),
                ('phone', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]