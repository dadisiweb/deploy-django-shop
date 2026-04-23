from django.core.management.base import BaseCommand
from shop.models import Product
from django.utils import timezone


class Command(BaseCommand):
    help = "Seed 30 clothing products into database"

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()

        products = [
            ("White T-Shirt", "Basic cotton tee", 800, 10),
            ("Black Oversized Tee", "Streetwear fit", 900, 10),
            ("Graphic Tee", "Printed design shirt", 950, 10),
            ("Polo Shirt Navy", "Smart casual polo", 1200, 10),
            ("Oxford Shirt", "Formal slim fit shirt", 1500, 10),

            ("Linen Shirt", "Light summer shirt", 1400, 10),
            ("Hoodie Grey", "Warm cotton hoodie", 2000, 10),
            ("Black Hoodie", "Minimal hoodie", 2100, 10),
            ("Zip Hoodie", "Full zip hoodie", 2200, 10),
            ("Tank Top", "Gym sleeveless top", 600, 10),

            ("Blue Jeans", "Classic denim jeans", 1800, 10),
            ("Black Jeans", "Slim fit black denim", 1800, 10),
            ("Cargo Pants", "Utility pockets pants", 1900, 10),
            ("Joggers Grey", "Comfort sweatpants", 1300, 10),
            ("Chinos Beige", "Smart casual pants", 1600, 10),

            ("Shorts Denim", "Summer shorts", 900, 10),
            ("Sports Shorts", "Running shorts", 800, 10),
            ("Wide Leg Pants", "Fashion fit pants", 1700, 10),
            ("Denim Jacket", "Classic jacket", 2500, 10),
            ("Leather Jacket", "Premium biker jacket", 4500, 10),

            ("Bomber Jacket", "Street bomber style", 3000, 10),
            ("Windbreaker", "Light rain jacket", 2200, 10),
            ("Winter Coat", "Heavy warm coat", 5000, 10),
            ("Cap Black", "Baseball cap", 500, 10),
            ("Beanie Hat", "Winter hat", 450, 10),

            ("White Socks Pack", "3-pack socks", 300, 10),
            ("Sneakers White", "Casual shoes", 3500, 10),
            ("Slides Black", "Comfort slippers", 1200, 10),
            ("Belt Leather", "Formal belt", 800, 10),
            ("Backpack", "Daily travel bag", 1500, 10),
        ]

        for name, desc, price, stock in products:
            Product.objects.create(
                name=name,
                description=desc,
                price=price,
                stock=stock,
                created_at=timezone.now()
            )

        self.stdout.write(self.style.SUCCESS("✅ 30 products seeded successfully"))
