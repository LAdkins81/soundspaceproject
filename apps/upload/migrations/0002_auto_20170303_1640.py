# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.FileField(default='images/nosong.png', max_length=45, upload_to='album_images'),
        ),
    ]
