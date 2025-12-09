from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Ticket, Review
from .forms import TicketForm, ReviewForm


@login_required
def create_ticket(request):
    """
    Create a new ticket.
    """
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("home")  # Redirect to home or feed
    else:
        form = TicketForm()
    return render(
        request, "reviews/ticket_form.html", {"form": form, "title": "Créer un ticket"}
    )


@login_required
def update_ticket(request, ticket_id):
    """
    Update an existing ticket.
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket.user != request.user:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à modifier ce ticket.")

    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TicketForm(instance=ticket)
    return render(
        request,
        "reviews/ticket_form.html",
        {"form": form, "title": "Modifier le ticket"},
    )


@login_required
def delete_ticket(request, ticket_id):
    """
    Delete a ticket.
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à supprimer ce ticket.")

    if request.method == "POST":
        ticket.delete()
        return redirect("home")

    return render(request, "reviews/ticket_confirm_delete.html", {"ticket": ticket})


@login_required
def create_review(request, ticket_id):
    """
    Create a review for a specific ticket.
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect("home")
    else:
        form = ReviewForm()
    return render(
        request,
        "reviews/review_form.html",
        {"form": form, "ticket": ticket, "title": "Créer une critique"},
    )


@login_required
def update_review(request, review_id):
    """
    Update an existing review.
    """
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        return HttpResponseForbidden(
            "Vous n'êtes pas autorisé à modifier cette critique."
        )

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ReviewForm(instance=review)
    return render(
        request,
        "reviews/review_form.html",
        {"form": form, "ticket": review.ticket, "title": "Modifier la critique"},
    )


@login_required
def delete_review(request, review_id):
    """
    Delete a review.
    """
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden(
            "Vous n'êtes pas autorisé à supprimer cette critique."
        )

    if request.method == "POST":
        review.delete()
        return redirect("home")

    return render(request, "reviews/review_confirm_delete.html", {"review": review})


@login_required
def create_ticket_and_review(request):
    """
    Create a ticket and a review in one step.
    """
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect("home")
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    return render(
        request,
        "reviews/create_ticket_and_review.html",
        {
            "ticket_form": ticket_form,
            "review_form": review_form,
        },
    )
