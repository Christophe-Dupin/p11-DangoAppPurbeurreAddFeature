from django.test import TestCase
from django.urls import reverse


class AppView(TestCase):
    def test_legale_view(self):
        url = reverse("legale")
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/legale.html")
