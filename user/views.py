from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from rest_framework import views, status
from rest_framework.response import Response
from django.views import generic
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

from virgilbookstore.permissions import LoginRequiredPermission
from .models import Profile, ProfileNewsletter, ProfileOffer
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
            
            return HttpResponseRedirect(reverse('user:dashboard'))
        else:
            messages.warning(
                request, 'Erro, usuário ou senha inválidos!')
            return HttpResponseRedirect(reverse('user:login'))

    context = {
        'form': LoginForm()
        }

    return render(request, 'pages/login.html', context)


class AddProfileOffersView(views.APIView):
    queryset = ProfileOffer.objects.all()
    
    def post(self, request):
        if request.data.get('email'):
            self.queryset.get_or_create(email=request.data.get('email'))
            return Response({'message': 'E-mail adicionado para ofertas da Loja'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Erro'}, status=status.HTTP_400_BAD_REQUEST)


class AddProfileNewsletterView(views.APIView):
    queryset = ProfileNewsletter.objects.all()
    
    def post(self, request):
        name = request.data.get('name')
        if name:
            self.queryset.get_or_create(email=request.data.get('email'), name=name)
            return Response({'message': 'E-mail adicionado na Newsletter'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Erro'}, status=status.HTTP_400_BAD_REQUEST)


class DashBoardProfile(LoginRequiredPermission, generic.TemplateView):
    queryset = Profile.objects.all()
    template_name = 'pages/dashboard.html'


class LogoutView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'home:home'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


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
