from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':

        email = request.POST["email"]
        password = request.POST["password"]
        users = User.objects.get(email=email)
        user = authenticate(username=users.username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/auth')

        else:
            messages.success(request, "The email or password is incorrect. Try again...")
            return redirect('/')

