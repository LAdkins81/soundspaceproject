# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20170228_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.FileField(max_length=45, null=True, upload_to='album_images'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(upload_to='songs'),
        ),
    ]