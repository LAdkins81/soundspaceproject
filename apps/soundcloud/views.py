from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..upload.models import Song
from ..loginandreg.models import User
from .models import Comment, Relationship
from .forms import CommentForm, UpdateForm
from .utils import *

QUERY="search-query"

MODEL_MAP = {
    Song: ["title","genre","artist","description"],
    }

def index(request):
    users=User.objects.all()
    context = {
        'users':users,
        'all_songs': Song.objects.all().order_by('-created_at'),
        'comments': Comment.objects.all(),
        'commentForm': CommentForm(),
    }
    return render(request, 'soundcloud/index.html', context)

def logout(request):
    if request.method == 'POST':
        request.session.clear()
    return redirect(reverse('loginandreg:homepage'))

def update_profile(request, id):
    user = User.objects.get(id=id)
    context={
        'user':user,
        'updateForm': UpdateForm(),
    }
    if request.method == 'POST':
        User.objects.update_user(request.POST)
        return redirect(reverse('soundspace:stream'))
    return render(request, 'soundcloud/user.html', context)

def user(request, id):
    profile_user = User.objects.get(id=id)
    logged_on_user = User.objects.get(id=request.session['user_id'])
    try:
        context = {
            'profile_user': profile_user,
            'commentForm': CommentForm(),
            'following': Relationship.objects.get(following=profile_user, follower=logged_on_user),
            'num_followers': len(Relationship.objects.filter(following=profile_user)),
            'num_following': len(Relationship.objects.filter(follower=profile_user)),
            'all_songs': Song.objects.filter(user=profile_user).order_by('-created_at'),
        }
    except:
        context = {
            'profile_user': profile_user,
            'commentForm': CommentForm(),
            'num_followers': len(Relationship.objects.filter(following=profile_user)),
            'num_following': len(Relationship.objects.filter(follower=profile_user)),
            'all_songs': Song.objects.filter(user=profile_user).order_by('-created_at'),
        }
    return render(request, 'soundcloud/userinfo.html', context)

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

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        song_query = get_query(query_string, ['artist','description','genre','title'])
        found_entries = Song.objects.filter(song_query).order_by('-title')
    context={
        'query_string': query_string,
        'found_entries': found_entries
    }
    return render(request, 'soundcloud/search.html', context)
