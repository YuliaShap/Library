from django.urls import path, include
from rest_framework import routers

from order.views import UserOrderDetail
from user.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/', include('user.urls')),

]
