from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

from product.models import Category, Product
from product.tools.productcleaner import ProductCleaner
from product.tools.productdownloader import ProductDownloader

"""Add custom Commande to fill the db."""


class Command(BaseCommand):
    help = "Launch this commande if you want to populate the db"

    def handle(self, *args, **options):
        """Launcher to get product from API and clean the data."""
        product_downloader = ProductDownloader()
        product_cleaner = ProductCleaner()
        raw_products = product_downloader.get_product()
        final_products = product_cleaner.clean_data(raw_products)
        for final_product in final_products:
            try:
                product = Product(
                    barcode=final_product["code"],
                    product_name=final_product["product_name"],
                    url_page=final_product["url"],
                    image_url=final_product["image_url"],
                    image_nutrition_url=final_product["image_nutrition_url"],
                    nutrition_grade=final_product["nutriscore"],
                    lipide=final_product["lipide"],
                    saturated_lipide=final_product["saturated_lipide"],
                    sugar=final_product["sugar"],
                    salt=final_product["salt"],
                )
            except ValidationError:
                # Ignore products with ValidationError
                continue
            Product.objects.bulk_create([product], ignore_conflicts=True)
            for y in final_product["categories"]:
                categorie = Category(name=y)
                categorie.save()
                categorie.product.add(product)
