# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-20 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professional',
            name='born_date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]