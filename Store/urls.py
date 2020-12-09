from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from home import views
#from order import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('home.urls')),
    path('home/', include('home.urls')),

    path('contact/', views.contact, name='contact'),


    path('book/<int:id>/<slug:slug>', views.book_detail, name='book_detail'),
    path('genre/<int:id>/<slug:slug>',
         views.book_genre, name='book_genre'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
