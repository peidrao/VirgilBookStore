from django.db import models


class ShopCartStatusChoice(models.TextChoices):
    IN_CART = "IN_CART", "in_cart"
    REMOVED = "REMOVED", "removed"
    BOUGTH = "BOUGTH", "bought"
