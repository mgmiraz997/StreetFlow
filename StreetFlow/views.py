from django.contrib import auth, messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def home(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # SignUP
        if 'register' in request.POST:
            data = User.objects.create_user(username=username, email=email, password=password)
            data.save()
            error = "Registration successful! Please login."

        # Login
        if 'login' in request.POST:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.get_user()
                login(request.user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('index:list')
            else:
                form = AuthenticationForm()
            return redirect(request, 'home.html', {'form': form})

    return render(request, 'home.html', {'error': error})


def menu(request):
    return render(request, 'index.html')


def style(request):
    return render(request, 'style.css')
