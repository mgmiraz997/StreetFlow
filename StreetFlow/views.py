from django.contrib import auth, messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail


def home(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        data = User.objects.create_user(username=username, email=email, password=password)
        data.save()
        error = "Registration successful! Please login."

    return render(request, 'home.html', {'error': error})


def login_view(request):
    return redirect('/')


def index(request):
    return render(request, 'index.html')


def style(request):
    return render(request, 'style.css')


def contactus(request):
    return render(request, 'contactus.html')


def ticket(request):
    return render(request, 'ticket.html')


def map(request):
    return render(request, 'map.html')


def reserve(request):
    return render(request, 'reserve.html')


def sendmail(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        sendmail(
            'email',
            'subject',
            'message',
            "mahmudul.gony@gmail.com",
            ['email'],
            fail_silently=False,
        )
        message.info(request, "Mail send successfully")
        return render(request, 'contactus.html')
    else:
        messages.info(request, "Mail not send")
        return render(request, 'contactus.html')
