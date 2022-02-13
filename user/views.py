from django.contrib.auth import authenticate, login as auth_login, logout as logout_func
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from .models import UserProfile
from .forms import LoginAuthenticationForm, LoginForm, SignUpForm
from book.models import Genre, Comment
from order.models import Order


@login_required(login_url='/login')
def index(request):
    context = {
        'genre': Genre.objects.all(),
    }
    return render(request, 'user/profile_page.html', context)


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
            return HttpResponseRedirect(reverse('user:profile'))
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect(reverse('user:signup'))

    context = {
        'genre': Genre.objects.all(),
        'form': SignUpForm()}
    return render(request, 'user/signup_page.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return HttpResponseRedirect(reverse('user:profile'))
        else:
            messages.warning(
                request, 'Erro, usuário ou senha inválidos!')
            return HttpResponseRedirect(reverse('user:login'))

    context = {
        'genre': Genre.objects.all(),
        'form': LoginForm()
        }


    return render(request, 'user/login_page.html', context)


def logout(request):
    logout_func(request)
    return HttpResponseRedirect(reverse('home:index'))


@login_required(login_url='/login')
def user_comments(request):
    context = {
        'genre': Genre.objects.all(),
        'comments': Comment.objects.filter(user=request.user)
    }

    return render(request, 'user/user_comments.html', context)


@login_required(login_url='/login')
def user_deletecomment(request, id):
    Comment.objects.filter(user=request.user, id=id).delete()
    messages.success(request, 'Comentário deleteado!')
    return HttpResponseRedirect(reverse('user:user_comments'))


@login_required(login_url='/login')
def user_orders(request):
    context = {
        'genre': Genre.objects.all(),
        'order': Order.objects.filter(user=request.user),
    }

    return render(request, 'user/user_orders.html', context)


@login_required(login_url='/login')
def user_request(request):
    context = {
        'genre': Genre.objects.all(),
        'order': Order.objects.filter(user=request.user),
    }

    return render(request, 'user/user_request.html', context)


@login_required(login_url='/login')
def user_order_book(request):
    context = {
        'genre': Genre.objects.all(),
        'order': Order.objects.filter(user=request.user),
    }
    return render(request, 'user/user_order_books.html', context)
