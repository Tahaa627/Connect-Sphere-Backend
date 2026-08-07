from django.shortcuts import get_object_or_404

from apps.posts.models import Post
from .models import Like


def toggle_like(user, post_id):
    """
    Toggle a like for a post.
    Returns:
        (liked, like_count)
    """

    post = get_object_or_404(Post, id=post_id)

    like = Like.objects.filter(
        user=user,
        post=post
    ).first()

    if like:
        like.delete()

        return (
            False,
            post.likes.count(),
        )

    Like.objects.create(
        user=user,
        post=post,
    )

    return (
        True,
        post.likes.count(),
    )