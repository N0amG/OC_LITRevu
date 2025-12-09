from django.urls import path
from . import views

urlpatterns = [
    path('ticket/create/', views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/edit/', views.update_ticket, name='update_ticket'),
    path('ticket/<int:ticket_id>/delete/', views.delete_ticket, name='delete_ticket'),
    path('review/create/<int:ticket_id>/', views.create_review, name='create_review'),
    path('review/<int:review_id>/edit/', views.update_review, name='update_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('review/create_ticket_and_review/', views.create_ticket_and_review, name='create_ticket_and_review'),
]
