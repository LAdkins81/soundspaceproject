from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..upload.models import Song
from ..loginandreg.models import User
from .models import Comment
from .forms import CommentForm

def index(request):
    context = {
        'all_songs': Song.objects.all(),
        'comments': Comment.objects.all(),
        'commentForm': CommentForm()
    }
    return render(request, 'soundcloud/index.html', context)

def logout(request):
    if request.method == 'POST':
        request.session.clear()
    return redirect(reverse('loginandreg:homepage'))

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
