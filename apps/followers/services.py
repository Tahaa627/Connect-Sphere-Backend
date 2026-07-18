from django.contrib.auth import get_user_model
from django.db import IntegrityError

from .models import Follow

User = get_user_model()

def follow_user(follower, username):
    """
    Create a follow relationship.

    Parameters
    ----------
    follower : User
        The authenticated user.

    username : str
        Username of the user to follow.
    """

    try:
        following = User.objects.get(username=username)

    except User.DoesNotExist:
        return {
            "success": False,
            "message": "User does not exist.",
            "status": 404,
        }

    if follower == following:
        return {
            "success": False,
            "message": "You cannot follow yourself.",
            "status": 400,
        }

    try:

        follow = Follow.objects.create(
            follower=follower,
            following=following,
        )

    except IntegrityError:

        return {
            "success": False,
            "message": "You are already following this user.",
            "status": 400,
        }

    return {
        "success": True,
        "follow": follow,
        "status": 201,
    }