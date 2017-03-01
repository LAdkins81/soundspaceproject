from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..loginandreg.models import User

from .models import Song
from .forms import DocumentForm

def index(request):
    documents = Song.objects.all()
    context = {
        'docForm': DocumentForm()
    }
    return render(request, "upload/index.html", context)

def create(request):
    user = User.objects.get(id=request.session['user_id'])
    song = request.FILES['song']
    image = request.FILES['image']
    files= FileSystemStorage()
    name=files.save(song.name, song)
    look = files.save(image.name, image)
    location = files.url(name)
    Song.objects.create(user=user, artist=request.POST['artist'], description = request.POST['description'] , genre= request.POST['genre'] , title= request.POST['title'] , tags=request.POST['tags'] , image=request.FILES['image'] , song= request.FILES['song'], )
    messages.warning(request, "Thanks for your contribution!")
    return redirect(reverse('upload:index'))
