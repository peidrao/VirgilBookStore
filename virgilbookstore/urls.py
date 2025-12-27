from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


from order import views as OrderViews


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("user/", include("user.urls")),
    path("", include("book.urls")),
    path("", include("market.urls")),
    path("order/", include("order.urls")),
    path("shopcart/", OrderViews.shopcart, name="shopcart"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
