from django import forms

from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'song', 'genre', 'title', 'tags', 'image')
