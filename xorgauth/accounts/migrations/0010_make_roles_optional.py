# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_allow_dot_in_user_hrid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='members',
                                         to='accounts.Role', verbose_name='roles'),
        ),
    ]
