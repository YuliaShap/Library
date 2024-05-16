from functools import wraps

from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from .forms import *
from .models import CustomUser


def home(request):
    return render(request, 'authentication/home.html')


def registration(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return render(request, 'authentication/home.html', {'name': user.first_name})
    else:
        form = AuthForm()
    return render(request, 'authentication/index.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                name = user.first_name
                return render(request, 'authentication/home.html', {'name': name})
            else:
                return render(request, 'authentication/login.html', {'form': form, 'error_message': 'Invalid email or password.'})
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def librarian_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user.role)

            if request.user.role == 1:
                return view_func(request, *args, **kwargs)

        return HttpResponseForbidden("Sorry! Only librarians can see this page.")

    return _wrapped_view


