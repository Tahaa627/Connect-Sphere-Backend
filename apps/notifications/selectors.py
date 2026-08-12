from .models import Notification
from django.shortcuts import get_object_or_404

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

def get_notification(notification_id, user):
    """
    Return a notification belonging to the authenticated user.
    """

    return get_object_or_404(
        Notification,
        id=notification_id,
        recipient=user,
    )