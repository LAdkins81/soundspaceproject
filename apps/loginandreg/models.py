from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import bcrypt
import datetime
# Create your models here.

class gender(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

onlyLetters = RegexValidator(r'^[a-zA-Z ]+$', message='Must be letters only.')
def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError('Must be longer than 2 characters'.format(value))

class UserManager(models.Manager):
    def login(self, object):
        email = object['email']
        password = object['password']
        user = User.objects.get(email=email)
        pw_hash = bcrypt.hashpw(password.encode(), user.password.encode())
        if pw_hash == user.password:
            return {'username': user.alias, 'uid': user.id}
        else:
            return {'error': 'Username/Password does not match.'}

    def register(self, object, **kwargs):
        alias = object['alias']
        email = object['email']
        password = object['password']
        age = object['age']
        gender = object['gender']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(alias=alias, email=email, password=pw_hash, age=age, gender=gender)
        user = User.objects.get(email=email)
        return {'success': 'You have registered succesfully!', 'uid': user.id}

class User(models.Model):
    alias = models.CharField(max_length=55, validators=[validateLengthGreaterThanTwo, onlyLetters])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    age = models.PostiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
