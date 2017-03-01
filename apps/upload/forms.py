from django import forms
from .models import Song

GENRE_CHOICES = (
    ('Alternative Rock', 'Alternative Rock'),
    ('Ambient', 'Ambient'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Comedy', 'Comedy'),
    ('Dance/EDM', 'Dance/EDM'),
    ('Drum & Bass', 'Drum & Bass'),
    ('Dubstep', 'Dubstep'),
    ('Electronic', 'Electronic'),
    ('Folk', 'Folk'),
    ('Hip Hop & Rap', 'Hip Hop & Rap'),
    ('House', 'House'),
    ('Indie', 'Indie'),
    ('Latin', 'Latin'),
    ('Metal', 'Metal'),
    ('Piano', 'Piano'),
    ('R&B & Soul', 'R&B & Soul'),
    ('Rock', 'Rock'),
    ('Soundtrack', 'Soundtrack'),
    ('Techno', 'Techno'),
    ('Trance', 'Trance'),
    ('Trap', 'Trap'),
    ('World', 'World'),
)

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ('song', 'title', 'artist', 'description', 'tags', 'image')
        labels = {

        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
            'tags': forms.Textarea(attrs={'rows': 1, 'cols': 40})
          }
    genre = forms.ChoiceField(choices=GENRE_CHOICES, required=False)
