from django.shortcuts import render

from app.form import Search


def home(request):
    """Define route for home Page."""
    search = Search()
    context = {"search": search}
    return render(request, "app/home.html", context)


def legale(request):
    """[summary]

    :param request: request object from django
    :type request: HTTPResponse
    :return: return a template with specifique context
    :rtype: render
    """
    return render(request, "app/legale.html")
