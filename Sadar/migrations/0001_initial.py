# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sadar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Sadar Name')),
                ('location', geoposition.fields.GeopositionField(default='28,77', max_length=42, verbose_name='Location of Sadar')),
                ('marker', models.ImageField(upload_to='Sadar/static/img', verbose_name='img')),
            ],
        ),
    ]