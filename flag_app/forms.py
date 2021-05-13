from django import forms


class SearchForm(forms.Form):
    country = forms.CharField(label='Search Your counrty',
                              max_length=100)

