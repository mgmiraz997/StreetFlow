from django.shortcuts import render
from map.models import Vehicle


def map_view(request):
    context = {'vehicles': list(Vehicle.objects.values('latitude', 'longitude'))}
    return render(request, 'map.html', context)
