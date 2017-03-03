from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import bcrypt
import datetime

onlyLetters = RegexValidator(r'^[a-zA-Z ]+$', message='Must be letters only.')
def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError('Must be longer than 2 characters'.format(value))

class UserManager(models.Manager):
    def login(self, object):
        email = object['email']
        password = object['password']
        try:
            user = User.objects.get(email=email)
            pw_hash = bcrypt.hashpw(password.encode(), user.password.encode())
            if pw_hash == user.password:
                return {'username': user.name, 'uid': user.id}
        except:
            return {'error': 'Username/Password does not match.'}

    def register(self, object, **kwargs):
        name = object['name']
        email = object['email']
        password = object['password']
        age = object['age']
        gender = object['gender']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(name=name, email=email, password=pw_hash, age=age, gender=gender)
        user = User.objects.get(email=email)
        return {'uid': user.id, 'user_name':user.name}

    def update_user(self, info, files, **kwargs):
        confirm = info['confirm_current_password']
        new_password = info['new_password']
        new_pw_hash = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
        user = User.objects.get(id=info['updateid'])

        try:
            pw_hash = bcrypt.hashpw(confirm.encode(), user.password.encode())
            if pw_hash == user.password:
                try:
                    user.name = info['name']
                    user.gender = info['gender']
                    user.email = info['email']
                    user.password = new_pw_hash
                    user.age = info['age']
                    user.image= files['picture']
                    user.description = info['description']
                    user.save()
                    return {'success': 'User information has been updated!'}
                except:
                    return {'error': 'ERROR'}
        except:
            return {'error': 'Username/Password does not match.'}

class User(models.Model):
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        )
    name = models.CharField(max_length=55, validators=[validateLengthGreaterThanTwo, onlyLetters])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    image = models.FileField(upload_to='profileimage', default='profileimage/default-profile-picture.jpeg')
    description= models.TextField(max_length=2000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
