from django.urls import path
from . import views

urlpatterns = [
    path("", views.redirect_view, name="redirect"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("home/", views.home_view, name="home"),
]
