from app.form import Search

"""Add new context processor template django."""


def search_form(request):
    return {"search_form": Search()}
