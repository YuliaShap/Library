"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from authentication.views import *
from author.views import *
from django.contrib import admin
from authentication.views import user_login
from django.urls import path, include
from order.views import *

from book import views
from book.views import *
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('authors/', authors, name='authors'),
    path('all_users/', all_users, name='all_users'),
    path('users/', users, name='users'),
    path('librarians/', librarians, name='librarians'),
    path('new_author/', new_author, name='new_author'),
    path('remove_author/<int:author_id>/', remove_author, name='remove_author'),
    path('books/', book, name='books'),
    path('books/info/<int:book_id>/', book_info, name='book_info'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('orders', orders, name='orders'),
    path('my_orders', all_user_orders, name='all_user_orders'),
    path('create_order', create_order, name='create_order'),
    path('delete_order/<int:order_id>/', delete_order, name='delete_order')


]
