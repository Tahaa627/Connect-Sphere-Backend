from .models import Notification


def create_notification(recipient,sender,notification_type,message,):
    """
    Create a notification unless the sender
    and recipient are the same user.
    """

    if recipient == sender:
        return None

    return Notification.objects.create(
        recipient=recipient,
        sender=sender,
        notification_type=notification_type,
        message=message,
    )