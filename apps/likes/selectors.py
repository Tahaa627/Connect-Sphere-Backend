from .models import Like


def get_post_likes(post_id):
    """
    Return all likes for a post.
    """

    return (
        Like.objects
        .filter(post_id=post_id)
        .select_related("user")
        .order_by("-created_at")
    )

from django.contrib.auth import get_user_model

User = get_user_model()


def get_users_who_liked(post_id):

    return (
        User.objects
        .filter(
            likes__post_id=post_id
        )
        .distinct()
    )