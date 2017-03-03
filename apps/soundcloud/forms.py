from django import forms
from ..loginandreg.models import User
from ..upload.models import *
from .models import Comment
from django.utils.translation import ugettext_lazy as _

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'genre', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 1, 'cols': 20})
          }
        labels = {
            'comment':_(''),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 2, 'cols': 40})
          }
        labels = {
            'comment':_(''),
        }

class UpdateForm(forms.Form):
    GENDER_CHOICES = (
            ('', '--------'),
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        )
    name = forms.CharField(required=False, max_length=45)
    picture = forms.FileField(required=False)
    email = forms.CharField(required=True)
    age = forms.IntegerField(required=False)
    gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES)
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
    password = forms.CharField(required=True, widget=forms.PasswordInput())
