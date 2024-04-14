from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':

        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index.html')

        else:
            messages.success(request, "The email or password is incorrect. Try again...")
            return redirect('home')


    else:
        render(request,'authenticate/login.html',{})
