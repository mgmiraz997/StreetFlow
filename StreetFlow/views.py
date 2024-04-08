from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        data = User.objects.create_user(username=username, email=email, password=password)
        data.save()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('menu')
    return render(request, 'home.html')


def menu(request):
    return render(request, 'menu.html')


def style(request):
    return render(request, 'style.css')