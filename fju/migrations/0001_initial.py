# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-15 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Students',
                'verbose_name': 'Student',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Universities',
                'verbose_name': 'University',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fju.University'),
        ),
    ]
