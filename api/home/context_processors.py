from book.models import Genre, Writer
from home.models import Banner
from market.models import CartItem, WishList


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
    data = {}
    if request.user.is_authenticated:
        data["wishlist"] = WishList.objects.filter(
            profile=request.user, is_active=True
        ).count()
    else:
        data["wishlist"] = 0

    return data


def get_cart_count(request):
    if request.user.is_authenticated:
        return {"cart": CartItem.objects.filter(profile=request.user).count()}
    return {"cart": 0}
