from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.http import JsonResponse

from product.models import Category, Favorite, Product


class UserSearchView(View):
    def post(self, request, *args, **kwargs):
        product_request = request.POST["search"]
        print(product_request)
        products = Product.objects.filter(
            product_name__icontains=product_request
        )
        return render(
            request,
            "product/search.html",
            {"products": products, "product_request": product_request},
        )


def substitute(request, barcode):
    product = get_object_or_404(Product, barcode=barcode)
    substitut = (
        Product.objects.filter(
            category__name__in=product.category.all().values("name")
        )
        .order_by("nutrition_grade")
        .distinct()[:9]
    )
    return render(
        request,
        "product/substitute.html",
        {"substitut": substitut, "product": product},
    )


@login_required(login_url="login")
def add_favorite(request, barcode, favorisBarcode):
    try:
        product = get_object_or_404(Product, barcode=barcode)
        substitut = get_object_or_404(Product, barcode=barcode)
        favoris = Favorite(
            substitute_product=substitut,
            products_substitute=product,
            user_substitute=request.user,
        )
    except (IntegrityError, Product.DoesNotExist):
        messages.info(request, "Produit ou substitut inexistant !")
        return redirect("/")
    try:
        favoris.save()
    except IntegrityError:
        messages.info(request, "Ce favori existe déjà !")
    return redirect("user_favorite")


@login_required(login_url="login")
def user_favorite(request):
    get_favoris_by_user = Favorite.objects.filter(user_substitute=request.user)
    return render(
        request,
        "product/favorite.html",
        {"get_favoris_by_user": get_favoris_by_user},
    )


@login_required(login_url="login")
def details_product(request, favorisBarcode):
    selected_product = get_object_or_404(Product, barcode=favorisBarcode)
    return render(
        request,
        "product/detail.html",
        {"selected_product": selected_product},
    )


def autocomplete(request):
    if "term" in request.GET:
        query = Product.objects.filter(
            product_name__icontains=request.GET.get("term")
        ).distinct()
        result = [i.product_name for i in query]
        return JsonResponse(result, safe=False)