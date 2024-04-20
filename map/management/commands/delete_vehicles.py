from django.core.management.base import BaseCommand
from map.models import Vehicle


class Command(BaseCommand):
    help = 'Deletes all vehicle objects from the database'

    def handle(self, *args, **kwargs):
        # Get the count of vehicles before deletion for the message
        count_before_deletion = Vehicle.objects.count()

        # Delete all vehicles
        Vehicle.objects.all().delete()

        # Get the count of vehicles after deletion for the message
        count_after_deletion = Vehicle.objects.count()

        # Print the result
        print(f"Deleted {count_before_deletion} vehicles from the database.")
        print(f"{count_after_deletion} vehicles now remain in the database.")
