from .models import Notification


def get_user_notifications(user):
    """
    Return all notifications for the authenticated user.
    """

    return (
        Notification.objects
        .filter(recipient=user)
        .select_related("sender")
        .order_by("-created_at")
    )