# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-07 03:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RentApp', '0002_property_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='related_sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RentApp.UrbanizedSector'),
        ),
    ]
