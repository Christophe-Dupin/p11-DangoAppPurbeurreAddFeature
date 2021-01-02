from django import forms

"""Create a form class for research."""


class Search(forms.Form):
    """[summary]

    :param forms: legacy from Form class of django
    :type forms: form
    """

    search = forms.CharField(widget=forms.Textarea, label="", max_length=100)
