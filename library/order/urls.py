from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import orders, all_user_orders, create_order, delete_order, OrderViewSet

router_order = DefaultRouter()
router_order.register(r'order', OrderViewSet)


urlpatterns = [
    path('orders', orders, name='orders'),
    path('my_orders', all_user_orders, name='all_user_orders'),
    path('create_order', create_order, name='create_order'),
    path('delete_order/<int:order_id>/', delete_order, name='delete_order'),
]
