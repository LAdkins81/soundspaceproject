from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Document
from .forms import DocumentForm


# Create your views here.
def index(request):
    documents = Document.objects.all()
    return render(request, "upload/index.html")

def create(request):
    song = request.FILES['song']
    image = request.FILES['image']
    files= FileSystemStorage()
    name=files.save(song.name, song)
    look = files.save(image.name, image)
    location = files.url(name)
    Document.objects.create(description = request.POST['description'] , genre= request.POST['genre'] , title= request.POST['title'] , tags=request.POST['tags'] , image=request.FILES['image'] , song= request.FILES['song'], )
    messages.warning(request, "Thanks for your contribution!")
    return redirect(reverse('upload:index'))
