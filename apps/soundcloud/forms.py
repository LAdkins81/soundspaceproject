from django import forms
from .models import Comment
from django.utils.translation import ugettext_lazy as _

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
