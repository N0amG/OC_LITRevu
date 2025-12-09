from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from reviews.models import Ticket, Review


def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Rediriger vers la page d'accueil après connexion
    else:
        form = AuthenticationForm()
    return render(request, "authentication/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "authentication/signup.html", {"form": form})


def home_view(request):
    tickets = Ticket.objects.all().order_by("-time_created")
    reviews = Review.objects.all().order_by("-time_created")
    if not request.user.is_authenticated:
        return redirect("login")
    return render(
        request, "authentication/home.html", {"tickets": tickets, "reviews": reviews}
    )


def redirect_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        return redirect("login")
