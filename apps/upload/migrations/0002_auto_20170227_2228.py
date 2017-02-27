# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document',
            new_name='song',
        ),
        migrations.AddField(
            model_name='document',
            name='genre',
            field=models.CharField(default=0, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='image',
            field=models.FileField(default=0, max_length=45, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.CharField(default=0, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default=0, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
