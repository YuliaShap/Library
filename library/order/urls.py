from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_orders, name='all_orders'),
    path('my_orders', views.all_user_orders, name='all_user_orders'),
    path('create_order', views.create_order, name='create_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order')
]