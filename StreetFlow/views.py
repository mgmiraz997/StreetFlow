from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def style(request):
    return render(request, template_name='style.css')
