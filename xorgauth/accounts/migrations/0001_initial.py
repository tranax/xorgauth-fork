# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-02 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid
import xorgauth.utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')),
                ('hrid', models.SlugField(unique=True, verbose_name='human-readable identifier')),
                ('fullname', xorgauth.utils.fields.UnboundedCharField(help_text='Name to display to other users', verbose_name='full name')),  # noqa: E501
                ('preferred_name', xorgauth.utils.fields.UnboundedCharField(help_text='Name used when addressing the user', verbose_name='preferred name')),  # noqa: E501
                ('main_email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
            ],
            options={
                'verbose_name_plural': 'user accounts',
                'verbose_name': 'user account',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.BooleanField(default=False, editable=False, verbose_name='system role')),
                ('hrid', models.SlugField(unique=True, verbose_name='human-readable identifier')),
                ('display', xorgauth.utils.fields.UnboundedCharField(unique=True, verbose_name='display name')),
            ],
            options={
                'verbose_name_plural': 'roles',
                'verbose_name': 'role',
            },
        ),
        migrations.CreateModel(
            name='UserAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email alias')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliases', to='accounts.User', verbose_name='user')),  # noqa: E501
            ],
            options={
                'verbose_name_plural': 'user aliases',
                'verbose_name': 'user alias',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(related_name='members', to='accounts.Role', verbose_name='roles'),
        ),
    ]
