from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


def search_users(query):
    """
    Search users by username,
    first name or last name.
    """

    return (
        User.objects
        .filter(
            Q(username__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
        )
        .order_by("username")
    )