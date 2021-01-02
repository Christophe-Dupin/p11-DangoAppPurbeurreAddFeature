from django.db import models

from user.models import User

"""Declare Product Model to django."""


class Product(models.Model):
    """Define product models.

    :param models: Define product fields
    :type models: Model
    :return: Product name object
    :rtype: [type]
    """

    barcode = models.CharField(max_length=20, primary_key=True)
    product_name = models.CharField(max_length=150)
    url_page = models.URLField()
    image_url = models.URLField()
    image_nutrition_url = models.URLField()
    nutrition_grade = models.CharField(max_length=1)
    lipide = models.FloatField(blank=True, default=0)
    saturated_lipide = models.FloatField(blank=True, default=0)
    sugar = models.FloatField(blank=True, default=0)
    salt = models.FloatField(blank=True, default=0)

    def __str__(self):
        return self.product_name


"""Declare Category Model to django."""


class Category(models.Model):
    """Define Category models.

    :param models:  Define Category fields
    :type models: Model
    :return: Category name object
    :rtype: Category
    """

    name = models.CharField(max_length=1)
    product = models.ManyToManyField(Product, related_name="category")

    def __str__(self):
        return self.name


"""Declare Favorite Model to django."""


class Favorite(models.Model):
    """Define Favorite models.

    :param models: Model
    :type models: Model
    """

    substitute_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="substitute"
    )
    products_substitute = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product"
    )
    user_substitute = models.ForeignKey(User, on_delete=models.CASCADE)
