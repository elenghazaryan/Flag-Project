from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import requests
from .forms import SearchForm
# Create your views here.


def get_flag_url(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if not form.is_valid():
            return HttpResponse("<h1>You're not correct</h1")
    else:
        form = SearchForm()
    c_name = form.cleaned_data.get("country")
    url = "https://restcountries.eu/rest/v2/name/{}".format(c_name)
    answer = requests.get(url).json()
    context = {
        "answer": answer[0]["flag"],
        "form": form,
        "country": c_name
    }
    return render(request, 'index.html', context)


