import requests


class ProductDownloader:
    """Class responsible of the download data from the API."""

    def __init__(self):
        """Define the number of product by page and response format."""
        self._page_size = 100
        self._json = 1
        self.categories = [
            "Plats préparés",
            "Fromages",
            "Desserts",
            "Viandes",
            "Boissons",
            "Produits laitiers",
        ]
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl?"

    def get_product(self):
        """Get some product from specifique catégorie."""
        # Iterate through the categories hardcode in the config.py
        all_products = []
        try:
            for category in self.categories:
                config = {
                    "action": "process",
                    "tagtype_0": "categories",
                    "tag_0": category,
                    "tag_contains_0": "contains",
                    "page_size": self._page_size,
                    "json": self._json,
                }
                # get all the url for the product for all the categories
                res = requests.get(self.url, params=config)
                if res.status_code == 200:
                    # Convert everything to json format
                    results = res.json()
                    # Add all the data with the key product
                    products = results["products"]
                    # add the product into the liste
                    all_products.extend(products)
        # Manage if there is a HTTP error
        except requests.exceptions.HTTPError as err:
            print("Http error:", err)
        # Manage if there is a connection error
        except requests.exceptions.ConnectionError as errc:
            print("You have a connection error: ", errc)
        return all_products
