from .models import ShopCart


def cart_count(request):
    if request.user.is_authenticated:
        return {
            "cart_count": ShopCart.objects.filter(profile=request.user).count()
        }
    return {"cart_count": 0}
