from django.urls import path
from . import views

urlpatterns = [
    path('', views.follow_users, name='follow_users'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
    path('remove_follower/<int:user_id>/', views.remove_follower, name='remove_follower'),
    path('block/<int:user_id>/', views.block_user, name='block_user'),
    path('unblock/<int:user_id>/', views.unblock_user, name='unblock_user'),
    path('search/', views.search_users, name='search_users'),
]
