from functools import wraps

from django.http import HttpResponseForbidden
from django.shortcuts import render

from authentication.models import CustomUser


def librarian_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user.role)

            if request.user.role == 1:
                return view_func(request, *args, **kwargs)

        return HttpResponseForbidden("Sorry! Only librarians can see this page.")

    return _wrapped_view


@librarian_required
def all_users(request):
    users_list = CustomUser.objects.all()
    print(users_list)
    return render(request, 'user/all_users.html', {'users_list': users_list})


def librarians(request):
    librarians_list = CustomUser.objects.filter(role=1)
    return render(request, 'user/librarians.html', {'librarians_list': librarians_list})


def users(request):
    users_list = CustomUser.objects.filter(role=0)
    return render(request, 'user/users.html', {'users_list': users_list})
