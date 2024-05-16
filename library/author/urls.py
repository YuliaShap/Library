from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import authors, new_author, remove_author, AuthorViewSet

router_author = DefaultRouter()
router_author.register(r'order', AuthorViewSet)


urlpatterns = [
    path('authors/', authors, name='authors'),
    path('new_author/', new_author, name='new_author'),
    path('remove_author/<int:author_id>/', remove_author, name='remove_author'),
]


