from django.urls import path

from product.views import UserSearchView

from . import views

urlpatterns = [
    path("search/", UserSearchView.as_view(), name="get_product"),
    path("substitute/<int:barcode>", views.substitute, name="substitute"),
    path(
        "add_favorite/<int:barcode>/<int:favorisBarcode>/",
        views.add_favorite,
        name="add_favorite",
    ),
    path("user_favorite/", views.user_favorite, name="user_favorite"),
    path("detail/<int:favorisBarcode>", views.details_product, name="detail"),
    path("autocomplete", views.autocomplete, name="autocomplete"),
]
