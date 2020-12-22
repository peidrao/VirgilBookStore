from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages

from .models import Comment
from .forms import CommentForm

# Create your views here.


def index(request):
    return HttpResponseRedirect('/')


def add_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.book_id = id

            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(
                request, 'Sua avaliação foi envianda com sucesso!')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
