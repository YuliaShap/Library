from django.urls import path
from .views import book, book_info, edit_book
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router_book = DefaultRouter()
router_book.register(r'book', BookViewSet)

urlpatterns = [
    path('books/', book, name='books'),
    path('books/info/<int:book_id>/', book_info, name='book_info'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
]
