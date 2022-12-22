import json
from django.contrib.auth import authenticate, login as auth_login, logout as logout_func
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views, status
from rest_framework.response import Response

from .models import Profile, ProfileOffer
from .forms import LoginAuthenticationForm, LoginForm, SignUpForm
from book.models import Comment
from order.models import Order


@login_required(login_url='/login')
def index(request): 
    return render(request, 'user/profile_page.html')


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)

            data = Profile()
            data.save()
            messages.success(request, 'Conta criada com sucesso!')
            return HttpResponseRedirect(reverse('user:profile'))
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect(reverse('user:signup'))

    context = {
        'form': SignUpForm()
    }
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
        'form': LoginForm()
        }

    return render(request, 'user/login_page.html', context)


def logout(request):
    logout_func(request)
    return HttpResponseRedirect(reverse('home:index'))


class AddProfileOffersView(views.APIView):
    queryset = ProfileOffer.objects.all()
    
    def post(self, request):
        if request.data.get('email'):
            self.queryset.get_or_create(email=request.data.get('email'))
            return Response({'message': 'E-mail adicionado para ofertas da Loja'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'Erro'}, status=status.HTTP_400_BAD_REQUEST)


@login_required(login_url='/login')
def user_comments(request):
    context = {
        'comments': Comment.objects.filter(user=request.user)
    }

    return render(request, 'user/user_comments.html', context)


@login_required(login_url='/login')
def user_deletecomment(request, id):
    Comment.objects.filter(profile=request.user, id=id).delete()
    messages.success(request, 'Comentário deleteado!')
    return HttpResponseRedirect(reverse('user:user_comments'))


@login_required(login_url='/login')
def user_orders(request):
    context = {
        'order': Order.objects.filter(profile=request.user),
    }

    return render(request, 'user/user_orders.html', context)


@login_required(login_url='/login')
def user_request(request):
    context = {
        'order': Order.objects.filter(profile=request.user),
    }

    return render(request, 'user/user_request.html', context)


@login_required(login_url='/login')
def user_order_book(request):
    context = {
        'order': Order.objects.filter(profile=request.user),
    }
    return render(request, 'user/user_order_books.html', context)
