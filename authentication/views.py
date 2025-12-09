from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import CharField, Value, Q
from itertools import chain
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
    if not request.user.is_authenticated:
        return redirect("login")

    # Récupérer les utilisateurs suivis et l'utilisateur courant
    followed_users = [user.followed_user for user in request.user.following.all()]
    followed_users.append(request.user)

    # Récupérer les tickets
    tickets = Ticket.objects.filter(user__in=followed_users).annotate(
        content_type=Value("TICKET", CharField())
    )

    # Récupérer les reviews
    # Critiques des utilisateurs suivis + critiques de l'utilisateur courant + critiques
    # sur les tickets de l'utilisateur courant
    reviews = Review.objects.filter(
        Q(user__in=followed_users) | Q(ticket__user=request.user)
    ).annotate(content_type=Value("REVIEW", CharField()))

    # Combiner et trier par date de création décroissante
    feed = sorted(
        chain(tickets, reviews), key=lambda post: post.time_created, reverse=True
    )

    return render(request, "authentication/home.html", {"feed": feed})


def redirect_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        return redirect("login")
