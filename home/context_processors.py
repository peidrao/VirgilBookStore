from book.models import Genre
from home.models import Banner


def get_genres(request):
    genres = Genre.objects.filter(origin__isnull=True).order_by('title')

    return {'genres': genres}


def get_banners(request):
    banners = Banner.objects.filter(is_active=True)
    return {'banners': banners}