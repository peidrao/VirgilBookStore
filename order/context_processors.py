from .choices import ShopCartStatusChoice
from .models import ShopCart


def cart_count(request):
    if request.user.is_authenticated:
        return {
            "cart_count": ShopCart.objects.filter(profile=request.user, status=ShopCartStatusChoice.IN_CART).count()
        }
    return {"cart_count": 0}
