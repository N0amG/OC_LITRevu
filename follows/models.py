from django.db import models
from django.conf import settings

# Create your models here.


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following"
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "followed_user"], name="unique_user_follow"
            )
        ]


class UserBlocks(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blocking"
    )
    blocked_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blocked_by",
    )

    class Meta:
        unique_together = ("user", "blocked_user")


constraints = [
    models.UniqueConstraint(fields=["user", "blocked_user"], name="unique_user_block")
]
