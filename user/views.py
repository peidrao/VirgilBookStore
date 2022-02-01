from django.contrib.auth import authenticate, login as auth_login, logout as logout_func
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import SignUpForm
from book.models import Genre, Comment
from order.models import Order


@login_required(login_url='/login')
def index(request):
    context = {
        'genre':  Genre.objects.all(),
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

            data = UserProfile()
            data.user_id = request.user.id
            data.save()
            messages.success(request, 'Conta criada com sucesso!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')
    
    context = {
        'genre': Genre.objects.all(),
        'form': SignUpForm()}
    return render(request, 'signup_page.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            userprofile = UserProfile.objects.get(user_id=request.user.id)
            request.session['userimage'] = userprofile.image.url
            return HttpResponseRedirect('/profile')
        else:
            messages.warning(
                request, 'Login Error!! Username or password incorect')
            return HttpResponseRedirect('/login')
    
    context = {'genre': Genre.objects.all()}
    return render(request, 'login_page.html', context)


def logout(request):
    logout_func(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login')
def user_comments(request):
    context = {
        'genre': Genre.objects.all(),
        'comments': Comment.objects.filter(user=request.user)
    }

    return render(request, 'user_comments.html', context)


@login_required(login_url='/login')
def user_deletecomment(request, id):
    Comment.objects.filter(user=request.user, id=id).delete()
    messages.success(request, 'Comentário deleteado!')
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login')
def user_orders(request):
    context = {
        'genre': Genre.objects.all(),
        'order': Order.objects.filter(user=request.user),
    }

    return render(request, 'user_orders.html', context)


@login_required(login_url='/login')
def user_request(request):
    context = {
        'genre': Genre.objects.all(),
        'order': Order.objects.filter(user=request.user),
    }

    return render(request, 'user_request.html', context)


@login_required(login_url='/login')
def user_order_book(request):
    context = {
        'genre': Genre.objects.all(),
        'order': Order.objects.filter(user=request.user),
    }
    return render(request, 'user_order_books.html', context)
