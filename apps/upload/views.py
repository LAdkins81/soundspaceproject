from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..loginandreg.models import User

from .models import *
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
    cover_image = request.FILES.get('cover_image', 'images/nosong.png')
    new = Song.objects.create(user=user, artist=request.POST['artist'], description = request.POST['description'] , genre= request.POST['genre'] , title= request.POST['title'], cover_image=cover_image , song= request.FILES['song'], )
    added_tags= request.POST['tags']
    all_tags= added_tags.split(',')
    for new_tag in all_tags:
        tag, created = Tag.objects.get_or_create(name=new_tag.lower().strip())
        new.tags.add(tag)
    messages.warning(request, "Thanks for your contribution!")
    return redirect(reverse('upload:index'))

def add_playlist(request, id):

    song=Song.objects.get(id=id)
    try:
        user= User.objects.get(id=request.session['user_id'])
        playlist= user.user_playlists.get(id=request.POST['playlist_id'])

        playlist.songs.add(song)

        return redirect(reverse('upload:playlist_info', kwargs={'id':request.POST['playlist_id']}))
    except:
        playlist_id = request.POST.get('playlist_id', False)
        if playlist_id == False:
            messages.warning(request, "**Please create a playlist to add to!**")
            return redirect(reverse('soundspace:user', kwargs={'id':request.session['user_id']}))
        return redirect(reverse('upload:playlist_info', kwargs={'id':request.POST['playlist_id']}))

def create_playlist(request):
    user = User.objects.get(id=request.session['user_id'])
    Playlist.objects.create(name=request.POST['name'], genre= request.POST['genre'], description=request.POST['description'], user=user)
    return redirect(reverse('soundspace:user', kwargs={'id':request.session['user_id']}))

def delete_playlist_song(request, id):
    select=request.POST['playlist_id']
    playlist = Playlist.objects.get(id=select)
    song = Song.objects.get(id=id)
    playlist.songs.remove(song)
    return redirect(reverse('soundspace:user', kwargs={'id':request.session['user_id']}))

def playlist_info(request, id):
    playlist = Playlist.objects.get(id=id)
    songs=playlist.songs.all()
    user=playlist.user
    context={
        'user': user,
        'songs': songs,
        'playlist':playlist
    }
    if playlist.user_id != request.session['user_id']:
        return redirect(reverse('soundspace:user', kwargs={'id':request.session['user_id']}))
    return render(request, 'soundcloud/playlist.html', context)

def repost(request,id):
    try:
        Repost.objects.get(post_id=id, user_id=request.session['user_id'])
    except:
        Repost.objects.create(post_id=id,user_id=request.session['user_id'])
    return redirect(reverse('soundspace:user', kwargs={'id':request.session['user_id']}))

def remove_repost(request, id):
    user_repost= Repost.objects.get(user_id=request.session['user_id'], post_id=id).delete()
    return redirect(reverse('soundspace:user', kwargs={'id':request.session['user_id']}))
