from django.urls import path

from . import views


urlpatterns = [
    path('addcomment/<int:id>', views.add_comment, name='add_comment')
]
