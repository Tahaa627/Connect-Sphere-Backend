from django.conf import settings
from django.db import models

from apps.posts.models import Post


class Like(models.Model):
    """
    Represents a user liking a post.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="likes",
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="likes",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"],
                name="unique_user_like",
            )
        ]

    def __str__(self):
        return f"{self.user.username} liked Post {self.post.id}"