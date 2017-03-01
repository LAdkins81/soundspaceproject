from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import *
from .forms import DocumentForm


# Create your views here.
def index(request):
    documents = Song.objects.all()
    context = {
        'docForm': DocumentForm()
    }
    return render(request, "upload/index.html", context)

def create(request):
    song = request.FILES['song']
    image = request.FILES['image']
    files= FileSystemStorage()
    name=files.save(song.name, song)
    look = files.save(image.name, image)
    location = files.url(name)
    new = Song.objects.create(artist= request.POST['artist'], description = request.POST['description'] , genre= request.POST['genre'] , title= request.POST['title'], image=request.FILES['image'] , song= request.FILES['song'], )
    added_tags= request.POST['tags']
    all_tags= added_tags.split(',')
    for new_tag in all_tags:
        tag, created = Tag.objects.get_or_create(name=new_tag.lower().strip())
        new.tags.add(tag)

    messages.warning(request, "Thanks for your contribution!")
    return redirect(reverse('upload:index'))
