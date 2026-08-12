from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


def get_user(user_id):
    """
    Return a user by ID.
    """

    return get_object_or_404(
        User,
        id=user_id,
    )