from django.core.management.base import BaseCommand

from product.models import Category, Favorite, Product

"""Add custom Commande to clean the db."""


class Command(BaseCommand):
    """Add specifique commande to manage.py
    :param BaseCommand: Legacy from BaseCommand class
    :type BaseCommand: BaseCommand
    """

    help = "Clean all Product from the db"

    def handle(self, *args, **options):
        """Methode to launch the specifque commande."""
        Category.objects.all().delete()
        Product.objects.all().delete()
        Favorite.objects.all().delete()
