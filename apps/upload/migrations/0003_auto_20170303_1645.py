# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20170303_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='image',
        ),
        migrations.AddField(
            model_name='song',
            name='cover_image',
            field=models.FileField(default='images/nosong.png', upload_to='album_images'),
        ),
    ]