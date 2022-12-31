from book.models import Genre, Writer
from home.models import Banner
from market.models import WishList


def get_genres(request):
    genres = Genre.objects.filter(origin__isnull=True).order_by("title")

    return {"genres": genres}


def get_banners(request):
    banners = Banner.objects.filter(is_active=True)
    return {"banners": banners}


def get_writers(request):
    writers = Writer.objects.all()
    return {"writers": writers}


def get_wishlist_count(request):
    return {
        "wishlist": WishList.objects.filter(
            profile=request.user, is_active=True
        ).count()
    }
