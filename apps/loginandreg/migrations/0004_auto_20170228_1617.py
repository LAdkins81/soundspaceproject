# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginandreg', '0003_auto_20170228_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(null=True, upload_to='profileimage'),
        ),
    ]
