# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginandreg', '0001_initial'),
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loginandreg.User'),
        ),
    ]