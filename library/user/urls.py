from django.urls import path
from .views import all_users, users, librarians
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router_user = DefaultRouter()
router_user.register(r'user', UserViewSet)

urlpatterns = [
    path('all_users/', all_users, name='all_users'),
    path('users/', users, name='users'),
    path('librarians/', librarians, name='librarians'),
]
