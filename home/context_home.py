from book.models import Genre


def menu_genres(request):
    genres = Genre.objects.all()
    return dict(genre=genres)
