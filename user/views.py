from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as logout_func
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from book.models import Genre
from .forms import SignUpForm


@login_required(login_url='/login')
def index(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

    genre = Genre.objects.all()
    context = {
        'genre': genre,
        'profile': profile
    }
    return render(request, 'profile_page.html', context)


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = 'images/users/user.png'
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
    genre = Genre.objects.all()
    context = {'genre': genre, 'form': form}
    return render(request, 'signup_page.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            return HttpResponseRedirect('/profile')
        else:
            messages.warning(
                request, 'Login Error!! Username or password incorect')
            return HttpResponseRedirect('/login')

    genre = Genre.objects.all()
    context = {'genre': genre}
    return render(request, 'login_page.html', context)


def logout(request):
    logout_func(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login')
def user_comments(request):
    genre = Genre.objects.all()
    current_user = request.user
