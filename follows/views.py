from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import UserFollows
from .forms import FollowUserForm

from django.http import JsonResponse

User = get_user_model()


@login_required
def search_users(request):
    """
    Search for users by username (autocomplete).
    """
    query = request.GET.get("q", "")
    if len(query) > 0:
        users = User.objects.filter(username__icontains=query).exclude(
            id=request.user.id
        )[:10]
    else:
        users = User.objects.exclude(id=request.user.id)[:5]

    results = [{"username": user.username} for user in users]
    return JsonResponse(results, safe=False)


@login_required
def follow_users(request):
    """
    Display followed users and followers, and handle following new users.
    """
    if request.method == "POST":
        form = FollowUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            try:
                user_to_follow = User.objects.get(username=username)
                if user_to_follow == request.user:
                    messages.error(request, "Vous ne pouvez pas vous suivre vous-même.")
                elif UserFollows.objects.filter(
                    user=request.user, followed_user=user_to_follow
                ).exists():
                    messages.warning(request, f"Vous suivez déjà {username}.")
                else:
                    UserFollows.objects.create(
                        user=request.user, followed_user=user_to_follow
                    )
                    messages.success(request, f"Vous suivez maintenant {username}.")
            except User.DoesNotExist:
                # Should be handled by form validation but just in case
                messages.error(request, "Cet utilisateur n'existe pas.")
            return redirect("follow_users")
    else:
        form = FollowUserForm()

    following = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)

    return render(
        request,
        "follows/follow_users.html",
        {"form": form, "following": following, "followers": followers},
    )


@login_required
def unfollow_user(request, user_id):
    """
    Unfollow a user.
    """
    user_to_unfollow = get_object_or_404(User, id=user_id)
    follow_relation = UserFollows.objects.filter(
        user=request.user, followed_user=user_to_unfollow
    )

    if follow_relation.exists():
        follow_relation.delete()
        messages.success(request, f"Vous ne suivez plus {user_to_unfollow.username}.")
    return redirect("follow_users")
