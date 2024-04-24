"""
URL configuration for StreetFlow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth/', views.index, name='index'),
    path('streetflow1', include('streetflow1.urls')),
    path('members/', include('members.urls')),
    path('map2/', include('map.urls')),
    path('/contactus', views.contactus, name='contactus'),
    path('/ticket', views.ticket, name='ticket'),
    path('/map', views.map, name='map'),
    path('reserve', views.reserve, name='reserve'),
    path('', include('reserve.urls')),
    path('', include('ticket.urls')),
    path('ticket/',include('ticket.urls')),
    path('sendmail', views.sendmail, name='sendmail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
