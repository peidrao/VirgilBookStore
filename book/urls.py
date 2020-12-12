from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addcomment/<int:id>', views.add_comment, name='add_comment')
]
