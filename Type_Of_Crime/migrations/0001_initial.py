# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type_Of_Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Type of Crime')),
                ('img', models.ImageField(upload_to='Type_Of_Crime/static/mark', verbose_name='Marker Image')),
            ],
            options={
                'verbose_name_plural': 'Type Of Crime',
                'verbose_name': 'Type Of Crime',
            },
        ),
    ]