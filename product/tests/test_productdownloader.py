from unittest import mock

from django.test import TestCase
from requests import ConnectionError
from requests import HTTPError

from product.tools.productdownloader import ProductDownloader

product_downloader = ProductDownloader()


class MockRequestResponse:
    """Mocking the get request function."""

    def __init__(self, json_data, status_code):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code == 200:
            return True
        elif self.status_code in [404, 500]:
            raise HTTPError
        else:
            raise ConnectionError


class MockRequests:
    def __init__(self, data, status_code):
        self.data = data
        self.status_code = status_code

    def get(self, *args, **kwargs):
        return MockRequestResponse(self.data, self.status_code)


class DownloaderTests(TestCase):
    def test_download_product(self):
        product = {
            "products": [
                {
                    "nutriscore_grade": "d",
                    "code": "7622210449283",
                    "url": "https://fr.openfoodfacts.org/produit/chocolat-au-ble-complet",
                    "product_name": "Prince goût chocolat au blé complet",
                }
            ]
        }
        mock_requests_get = MockRequests(product, 200).get

        with mock.patch(
            "product.tools.productdownloader.requests.get", mock_requests_get
        ):
            result = product_downloader.get_product()
            # To do a checker avec aurelien
            # print(result[0])
            # print(product["products"])
            self.assertEqual([result[0]], product["products"])
