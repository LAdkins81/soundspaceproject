from __future__ import unicode_literals

import apps.loginandreg.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, validators=[apps.loginandreg.models.validateLengthGreaterThanTwo, django.core.validators.RegexValidator('^[a-zA-Z ]+$', message='Must be letters only.')])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('image', models.FileField(null=True, upload_to='profileimage')),
                ('description', models.TextField(max_length=2000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
