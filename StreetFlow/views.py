from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def home(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user is trying to register
        if 'register' in request.POST:
            data = User.objects.create_user(username=username, email=email, password=password)
            data.save()
            error = "Registration successful! Please login."

        # If the user is trying to log in
        elif 'login' in request.POST:
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('menu')
            else:
                error = "Invalid email or password"

    return render(request, 'home.html', {'error': error})


def menu(request):
    return render(request, 'menu.html')


def style(request):
    return render(request, 'style.css')
