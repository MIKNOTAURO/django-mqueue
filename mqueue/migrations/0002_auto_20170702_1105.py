# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mqueue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mevent',
            name='bucket',
            field=models.CharField(blank=True, max_length=60, verbose_name='Bucket'),
        ),
        migrations.AddField(
            model_name='mevent',
            name='data',
            field=jsonfield.fields.JSONField(blank=True, verbose_name='Data'),
        ),
    ]