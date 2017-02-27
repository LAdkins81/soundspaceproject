from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'soundcloud/index.html')

def logout(request):
    if request.method == 'POST':
        request.session.clear()
    return redirect(reverse('loginandreg:homepage'))
