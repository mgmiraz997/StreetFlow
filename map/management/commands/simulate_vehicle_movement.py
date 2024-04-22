import random
import time
from django.core.management.base import BaseCommand
from map.models import Vehicle


class Command(BaseCommand):
    help = 'Simulate vehicle movement'

    def handle(self, *args, **options):
        # Define the range of latitude and longitude variation
        let_lon_var = 0.01  # 0.01 degree is approximately 1.1km

        while True:
            print("Vehicle positions updating...")

            for vehicle in Vehicle.objects.all():
                vehicle.latitude = vehicle.latitude + random.uniform(-let_lon_var, let_lon_var)
                vehicle.longitude = vehicle.longitude + random.uniform(-let_lon_var, let_lon_var)
                vehicle.save()

            time.sleep(5)