from django.test import TestCase
from django.urls import reverse
from django.db.models.query import QuerySet
from app.form import Search
from product.models import Product, Favorite
from user.models import User


class ProductView(TestCase):
    def setUp(self):
        self.search = {"search": "jambon"}
        self.product = Product(
            barcode=3302740025136,
            product_name=" LE JAMBON ZERO NITRITE - 4 tr",
            url_page="toto",
            image_url="tutu",
            image_nutrition_url="https://static.openfoodfacts.org/images/products/330/274/002/5136/front_fr.87.400.jpg",
            nutrition_grade="c",
            lipide=float(0.2),
            saturated_lipide=float(0.4),
            sugar=float(0.6),
            salt=float(0.8),
        )
        self.favoris = Product(
            barcode=3095757369019,
            product_name=" LE JAMBON ZERO NITRITE - 4 tr",
            url_page="toto",
            image_url="tutu",
            image_nutrition_url="https://static.openfoodfacts.org/images/products/330/274/002/5136/front_fr.87.400.jpg",
            nutrition_grade="c",
            lipide=float(0.2),
            saturated_lipide=float(0.4),
            sugar=float(0.6),
            salt=float(0.8),
        )
        self.product.save()
        self.favoris.save()
        self.aurelien = User.objects.create_user(
            "aurelien", "aurelien@test.com", "aurelien"
        )

    def test_home_page(self):
        url = reverse("app-home")
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/home.html")
        self.assertEqual(type(response.context["search_form"]), Search)

    def test_home_page_search_product(self):
        url = reverse("get_product")
        response = self.client.post(url, self.search)
        self.failUnlessEqual(response.status_code, 200)
        self.assertEqual(type(response.context["products"]), QuerySet)
        self.assertTemplateUsed(response, "product/search.html")

    def test_substitute_display(self):
        url = reverse(
            "substitute",
            args=[
                self.product.barcode,
            ],
        )
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "product/substitute.html")
        self.assertEqual(type(response.context["substitut"]), QuerySet)

    def test_user_not_authenticated_redirect_to_login_page(self):
        url = reverse("user_favorite")
        login = "/user/login/?next=/product/user_favorite/"
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, "product/favorite.html")
        self.failUnlessEqual(response.status_code, 302)
        self.assertRedirects(response, login)

    def test_user_authenticated_have_access_to_favoris_area(self):
        self.client.login(username="aurelien", password="aurelien")
        url = reverse("user_favorite")
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "product/favorite.html")
        self.assertEqual(
            type(response.context["get_favoris_by_user"]), QuerySet
        )
        self.client.logout()

    def test_user_authenticated_add_favoris(self):
        url = reverse(
            "add_favorite",
            args=[self.product.barcode, self.favoris.barcode],
        )
        favoris = "/product/user_favorite/"
        self.client.login(username="aurelien", password="aurelien")
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 302)
        self.assertRedirects(response, favoris)
        query = Favorite.objects.filter(
            user_substitute=self.aurelien.id
        ).first()
        self.assertEquals(
            query.products_substitute.product_name, self.product.product_name
        )

    def test_details_product_user_not_authenticated(self):
        url = reverse("detail", args=[self.favoris.barcode])
        login = "/user/login/?next=/product/detail/3095757369019"
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 302)
        self.assertRedirects(response, login)

    def test_details_product_user_authenticated(self):
        url = reverse("detail", args=[self.favoris.barcode])
        self.client.login(username="aurelien", password="aurelien")
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "product/detail.html")
        self.assertEqual(type(response.context["selected_product"]), Product)
