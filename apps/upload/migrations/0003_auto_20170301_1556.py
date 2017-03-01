# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20170301_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='tags',
        ),
        migrations.AddField(
            model_name='song',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='songs', to='upload.Tag'),
        ),
    ]
