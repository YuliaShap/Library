
from django.urls import path, include
from authentication.views import home
from author.views import AuthorDetail
from book.views import BookDetail
from order.urls import router_order
from book.urls import router_book
from author.urls import router_author
from order.views import UserOrderDetail
from user.urls import router_user

urlpatterns = [
    path('', home, name='home'),
    path('api/v1/', include(router_user.urls)),
    path('api/v1/', include(router_order.urls)),
    path('api/v1/', include(router_book.urls)),
    path('api/v1/', include(router_author.urls)),
    path('api/v1/user/<int:user_id>/order/<int:order_id>/', UserOrderDetail.as_view(), name='user_order_detail'),
    path('api/v1/user/<int:user_id>/order/', UserOrderDetail.as_view(), name='user_order_create'),
    path('api/v1/book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('api/v1/author/<int:pk>/', AuthorDetail.as_view(), name='author-detail')
]
