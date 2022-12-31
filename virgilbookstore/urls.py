from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from order import views as OrderViews


urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include("home.urls")),
    path("user/", include("user.urls")),
    path("", include("book.urls")),
    path("", include("market.urls")),
    path("order/", include("order.urls")),
    path("shopcart/", OrderViews.shopcart, name="shopcart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
