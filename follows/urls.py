from django.urls import path
from . import views

urlpatterns = [
    path('', views.follow_users, name='follow_users'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
    path('search/', views.search_users, name='search_users'),
]
