from django.test import TestCase
from product.tools.productcleaner import ProductCleaner


class CleanerTests(TestCase):
    def test_clean_product(self):
        product = {
            "products": [
                {
                    "nutrition_grade_fr": "d",
                    "code": "7622210449283",
                    "url": "https://fr.openfoodfacts.org/produit/chocolat-au-ble-complet",
                    "product_name": "Prince goût chocolat au blé complet",
                    "image_nutrition_url": "https://fr.openfoodfacts.org/produit/chocolat-au-ble-complet",
                    "nutriments": {
                        "fat_100g": 0.2,
                        "saturated-fat_100g": 0.4,
                        "sugars_100g": 0.5,
                        "salt_100g": 0.4,
                    },
                    "categories": "toto",
                    "product_name_fr": "kiki",
                    "image_url": "https://fr.openfoodfacts.org/produit/chocolat-au-ble-complet",
                }
            ]
        }
        cleaner = ProductCleaner()
        result = cleaner.clean_data(product["products"])
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), len(product))
