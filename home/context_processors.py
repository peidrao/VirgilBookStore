from book.models import Genre


def menu_genres(request):
    genres = Genre.objects.filter(origin__isnull=True).order_by('title')
    return {'genres': genres}
