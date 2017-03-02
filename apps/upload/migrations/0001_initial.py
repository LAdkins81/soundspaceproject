# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 21:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginandreg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=255)),
                ('genre', models.CharField(max_length=45)),
                ('title', models.CharField(max_length=45)),
                ('artist', models.CharField(max_length=45)),
                ('image', models.FileField(max_length=45, null=True, upload_to='album_images')),
                ('song', models.FileField(upload_to='songs')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='songs', to='upload.Tag'),
        ),
        migrations.AddField(
            model_name='song',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loginandreg.User'),
        ),
    ]
