from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..upload.models import *
from ..loginandreg.models import *
from .models import *
from .forms import *
from .utils import *

QUERY="search-query"

MODEL_MAP = {
    Song: ["title","genre","artist","description"],
    }

def index(request):
    playlists= Playlist.objects.filter(user_id=request.session['user_id'])
    logged_on_user = User.objects.get(id=request.session['user_id'])
    likes = Like.objects.filter(user=logged_on_user)
    user_likes = {}
    for l in likes:
        if l.user_id == request.session['user_id']:
            user_likes[l.song_id] = True
    context = {
        'logged_on_user': logged_on_user,
        'commentForm': CommentForm(),
        'all_songs': Song.objects.all().order_by('-created_at'),
        'comments': Comment.objects.all(),
        'user_liked': user_likes,
        'playlists':playlists,
    }
    return render(request, 'soundcloud/index.html', context)

def logout(request):
    if request.method == 'POST':
        request.session.clear()
    return redirect(reverse('loginandreg:homepage'))

def song(request, id):
    logged_on_user = User.objects.get(id=request.session['user_id'])
    likes = Like.objects.filter(user=logged_on_user)
    user_likes = {}
    for l in likes:
        if l.user_id == request.session['user_id']:
            user_likes[l.song_id] = True
    context = {
        'commentForm': CommentForm(),
        'song': Song.objects.get(id=id),
        'user_liked': user_likes,
        'comments': Comment.objects.all(),
    }
    return render(request, 'soundcloud/song.html', context)

def user(request, id):
    profile_user = User.objects.get(id=id)
    logged_on_user = User.objects.get(id=request.session['user_id'])
    playlists= Playlist.objects.filter(user_id=id)
    all_songs= Song.objects.filter(user=profile_user).order_by('-created_at')
    num_followers= len(Relationship.objects.filter(following=profile_user))
    num_following= len(Relationship.objects.filter(follower=profile_user))
    user_follows= Relationship.objects.filter(following=profile_user).all().order_by('-id')[:5]
    user_followings=Relationship.objects.filter(follower=profile_user).all().order_by('-id')[:5]
    for song in all_songs:
        reposts = song.song_reposts.all()
        for repost in reposts:
            user= repost.user_id
            if profile_user.id == user:
                song.joined=True
            else:
                song.joined=False
    likes = Like.objects.filter(user=logged_on_user)
    user_likes = {}
    for l in likes:
        if l.user_id == request.session['user_id']:
            user_likes[l.song_id] = True
    context = {
            'reposts':Repost.objects.filter(user_id=id),
            'playlists':playlists,
            'profile_user': profile_user,
            'commentForm': CommentForm(),
            'playlistForm': PlaylistForm(),
            'num_followers': num_followers,
            'num_following': num_following,
            'all_songs': all_songs,
            'user_liked': user_likes,
            'user_follows':user_follows,
            'user_followings':user_followings,
            'comments': Comment.objects.all(),
            'following': Relationship.objects.filter(follower=logged_on_user, following=profile_user),
            }
    return render(request, 'soundcloud/userinfo.html', context)


def update_profile(request, id):
    user = User.objects.get(id=id)
    context={
        'user':user,
        'updateForm': UpdateForm(),
    }
    if request.method == 'POST':
        User.objects.update_user(request.POST, request.FILES)
        request.session['username'] = request.POST['name']
        return redirect(reverse('soundspace:update_profile', kwargs={'id':id}))
    return render(request, 'soundcloud/updateinfo.html', context)

def create_comment(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.session['user_id'])
        song = Song.objects.get(id=request.POST['song_id'])
        Comment.objects.create(user=user, song=song, comment=request.POST['comment'])
        return redirect(reverse('soundspace:stream'))

def delete_comment(request):
    if request.method == 'POST':
        Comment.objects.get(id=request.POST['comment_id']).delete()
        return redirect(reverse('soundspace:stream'))

def follow(request):
    if request.method == 'POST':
        profile_user_id = request.POST['followingid']
        response = Relationship.objects.follow(request.POST)
        return redirect(reverse('soundspace:user', kwargs={'id':profile_user_id}))

def unfollow(request):
    if request.method == 'POST':
        profile_user_id = request.POST['unfollowid']
        response = Relationship.objects.unfollow(request.POST)
        return redirect(reverse('soundspace:user', kwargs={'id':profile_user_id}))

def like(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        Like.objects.create_like(request.POST, user_id)
        return redirect(reverse('soundspace:stream'))

def unlike(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        Like.objects.unlike(request.POST, user_id)
        return redirect(reverse('soundspace:stream'))

def search(request):
    playlists= Playlist.objects.filter(user_id=request.session['user_id'])
    logged_on_user = User.objects.get(id=request.session['user_id'])
    likes = Like.objects.filter(user=logged_on_user)
    user_likes = {}
    for l in likes:
        if l.user_id == request.session['user_id']:
            user_likes[l.song_id] = True
    query_string = ''
    all_songs = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        song_query = get_query(query_string, ['artist','description','genre','title'])
        all_songs = Song.objects.filter(song_query).order_by('-title')
    context={
        'query_string': query_string,
        'all_songs': all_songs,
        'commentForm': CommentForm(),
        'comments': Comment.objects.all(),
        'user_liked': user_likes,
        'playlists':playlists,
    }
    return render(request, 'soundcloud/search.html', context)

def artist_info(request, name):
    playlists= Playlist.objects.filter(user_id=request.session['user_id'])
    songs=Song.objects.filter(artist__iexact=name)
    logged_on_user = User.objects.get(id=request.session['user_id'])
    likes = Like.objects.filter(user=logged_on_user)
    user_likes = {}
    for l in likes:
        if l.user_id == request.session['user_id']:
            user_likes[l.song_id] = True
    context={
        'songs':songs,
        'name':name,
        'commentForm': CommentForm(),
        'comments': Comment.objects.all(),
        'user_likeS': user_likes,
        'playlists':playlists,
    }
    return render(request, 'soundcloud/artist.html', context)
