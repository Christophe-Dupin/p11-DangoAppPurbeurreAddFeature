from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="app-home"),
    path("legale/", views.legale, name="legale"),
]
