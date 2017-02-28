from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import *

def index(request):
    users=User.objects.all()
    context={
        'users':users
    }
    return render(request, 'soundcloud/index.html', context)

def logout(request):
    if request.method == 'POST':
        request.session.clear()
    return redirect(reverse('loginandreg:homepage'))

def update(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        print user.id
        if len(request.POST['name']) >1:
            user.name= request.POST['name']
            request.session['username'] = user.name
            print user.name
        if len(request.POST['gender']) >1:
            user.gender= request.POST['gender']
        if len(request.POST['email']) >1:
            user.email=request.POST['email']
        if len(request.POST['newpassword']) >1:
            user.password=request.POST['newpassword']
        if len(request.POST['age']) >1:
            user.age=request.POST['age']
        if len(request.POST['description'])>1:
            user.description=request.POST['description']
        try:
            user.image=request.FILES['image']
        except:
            pass
        user.save()
        return redirect(reverse('soundspace:stream'))
    user = User.objects.get(id=id)
    context={
        'user':user
    }

    return render(request, 'soundcloud/user.html', context)

def user(request, id):
    user = User.objects.get(id=id)
    context={
        'user':user
    }
    return render(request, 'soundcloud/userinfo.html', context)
