from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {"title": "Beach House", "description": "A nice house by the beach", "price_per_night": 120.00, "location": "Mombasa"},
            {"title": "Mountain Cabin", "description": "A cozy cabin in the mountains", "price_per_night": 80.00, "location": "Mt. Kenya"},
            {"title": "City Apartment", "description": "Modern apartment in the city center", "price_per_night": 100.00, "location": "Nairobi"},
        ]

        for listing_data in sample_listings:
            listing, created = Listing.objects.get_or_create(**listing_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))
