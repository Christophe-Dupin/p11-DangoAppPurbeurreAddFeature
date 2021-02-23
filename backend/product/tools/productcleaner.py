class ProductCleaner:
    """Class responsible of the cleaning of the data."""

    def clean_data(self, data):
        """Methode to validate and clean the data from the API.

        :param data: [Object return from the get_product methode.]
        :type data: [ProductDownloader]
        """
        # Clean product empty list
        clean_product = []
        for x in data:
            # Check if the data is valide to avoid sql error
            if (
                "product_name_fr" in x
                and len(x["product_name"]) < 150
                and len(x["product_name"]) != 0
                and len(x["code"]) == 13
                and "nutrition_grade_fr" in x
                and "image_nutrition_url" in x
                and "fat_100g" in x["nutriments"]
                and "saturated-fat_100g" in x["nutriments"]
                and "sugars_100g" in x["nutriments"]
                and "salt_100g" in x["nutriments"]
                and len(x["url"]) != 0
                and len(x["categories"]) <= 150
                and len(x["categories"]) != 0
            ):
                i = {
                    "code": x["code"],
                    "product_name": x["product_name"],
                    "nutriscore": x["nutrition_grade_fr"],
                    "url": x["url"],
                    "image_url": x["image_url"],
                    "image_nutrition_url": x["image_nutrition_url"],
                    "lipide": x["nutriments"]["fat_100g"],
                    "saturated_lipide": x["nutriments"]["saturated-fat_100g"],
                    "sugar": x["nutriments"]["sugars_100g"],
                    "salt": x["nutriments"]["salt_100g"],
                    "categories": x["categories"].split(","),
                }
                clean_product.append(i)
        return clean_product
