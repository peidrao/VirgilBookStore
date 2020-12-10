from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from book.models import Genre
from .forms import SignUpForm
from .models import UserProfile
# Create your views here.


def index(request):
    return None


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = 'images/users/user.png'
            data.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
    genre = Genre.objects.all()
    context = {'genre': genre, 'form': form}
    return render(request, 'signup_page.html', context)
