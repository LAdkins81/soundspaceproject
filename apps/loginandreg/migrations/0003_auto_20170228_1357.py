# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginandreg', '0002_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(null=True, upload_to='apps/loginandreg/static/loginandreg/user'),
        ),
    ]