from django.shortcuts import render, redirect
from myApp.forms import PresidentForm, CountryForm
from myApp.models import President, Country


# Create your views here.
def home(request):
    president = President.objects.all()
    country = Country.objects.all()
    context = {
        "president": president,
        "country": country,
    }
    return render(request, "myApp/home.html", context)


def create_president(request):
    if request.method == "POST":
        form = PresidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PresidentForm()
    return render(request, "myApp/backoffice/forms/create_president.html", {"form": form})


def create_country(request):
    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CountryForm()
    return render(request, "myApp/backoffice/forms/create_country.html", {"form": form})

def users(request):
    return render(request, "myApp/users.html")