from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import User

def index(request):
    if 'user_id' in request.session:
        return redirect(reverse('soundspace:stream'))
    return render(request, 'loginandreg/index.html')

def login(request):
    context = {
        'loginForm': LoginForm()
    }
    if 'user_id' in request.session:
        return redirect(reverse('soundspace:stream'))
    return render(request, 'loginandreg/login.html', context)

def register(request):
    context = {
        'regForm': RegisterForm()
    }
    if 'user_id' in request.session:
        return redirect(reverse('soundspace:stream'))
    return render(request, 'loginandreg/register.html', context)

def register_user(request):
    if request.method == 'POST':
        regForm = RegisterForm(request.POST)
        messages.add_message(request, messages.ERROR, regForm.errors)
        if regForm.is_valid():
            response = User.objects.register(request.POST)
            request.session['username'] = response['user_name']
            request.session['user_id'] = response['uid']
            return redirect(reverse('soundspace:stream'))
        else:
            return redirect(reverse('loginandreg:register'))

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            response = User.objects.login(request.POST)
            if 'error' in response:
                messages.add_message(request, messages.ERROR, 'Username/Password does not match')
                return redirect(reverse('loginandreg:login'))
            else:
                user=User.objects.get(email=request.POST['email'])
                request.session['username'] = user.name
                request.session['user_id'] = user.id
                return redirect(reverse('soundspace:stream'))
