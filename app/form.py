from django import forms

"""Create a form class for research."""


class Search(forms.Form):
    """[summary]

    :param forms: legacy from Form class of django
    :type forms: form
    """

    search = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={"class": "search_id"}),
    )
