from django.test import TestCase
from django.urls import reverse
from django.db.models.query import QuerySet
from user.models import User


class UserView(TestCase):
    def setUp(self):
        self.aurelien = User.objects.create_user(
            "aurelien", "aurelien@test.com", "aurelien"
        )

    def test_register_view(self):
        url = reverse("register")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "user/register.html")

    def test_register_people(self):
        people = {
            "username": "sisi",
            "email": "sisi@test.com",
            "password": "testing1234",
        }

        url = reverse("register")
        login = "/user/login/?next=/user/profile/"
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.post(url, people)
        redirect = self.client.get(response.url)
        self.failUnlessEqual(redirect.status_code, 302)
        self.assertRedirects(redirect, login)
        query = User.objects.filter(username="sisi").first()
        self.assertEquals(query.username, people["username"])

    def test_login_people(self):
        url = reverse("login")
        home = "/"
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")
        post = self.client.post(
            url, {"username": "aurelien", "password": "aurelien"}
        )
        self.failUnlessEqual(post.status_code, 302)
        self.assertRedirects(post, home)
        self.assertIn("_auth_user_id", self.client.session)

    def test_profile_view(self):
        redirect = reverse("app-home")
        url = reverse("profile")
        self.client.login(username="aurelien", password="aurelien")
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
        post = self.client.post(
            url, {"username": "tutu", "email": "tutu@gmail.com"}
        )
        self.failUnlessEqual(post.status_code, 302)
        self.assertRedirects(post, redirect)
        query = User.objects.filter(username="tutu").first()
        self.assertEquals(query.username, "tutu")