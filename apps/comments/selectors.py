from django.db.models import Prefetch

from .models import Comment


def get_post_comments(post_id):
    """
    Return only top-level comments.
    Replies are loaded automatically.
    """

    return (
        Comment.objects
        .filter(
            post_id=post_id,
            parent__isnull=True,
        )
        .select_related("author")
        .prefetch_related(
            Prefetch(
                "replies",
                queryset=Comment.objects.select_related("author")
            )
        )
        .order_by("created_at")
    )