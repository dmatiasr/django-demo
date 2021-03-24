# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-06 18:55
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('lat', models.CharField(max_length=30, null=True)),
                ('lon', models.CharField(max_length=30, null=True)),
                ('location_point', django.contrib.gis.db.models.fields.PointField(default='POINT( 0.0 0.0 )', help_text='Represented as (longitude, latitude)', srid=4326)),
                ('type', models.CharField(blank=True, choices=[('house', 'house'), ('departament', 'departament'), ('local', 'local'), ('camping', 'camping')], max_length=50, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='property_updated_at')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='property_created_at')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UrbanizedSector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('polygon_representation', django.contrib.gis.db.models.fields.PolygonField(help_text='POLYGON((lon lat, lon lat, lon lat, lon lat, lon lat))', srid=4326)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='urbanized_sector_updated_at')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='urbanized_sector_created_at')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='urbanized_sector_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='urbanized_sector_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='related_sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RentApp.UrbanizedSector'),
        ),
        migrations.AddField(
            model_name='property',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]