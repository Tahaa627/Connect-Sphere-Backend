from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.likes.models import Like
from .models import Notification
from .services import create_notification

from apps.followers.models import Follow

@receiver(post_save, sender=Like)
def like_notification(sender, instance, created, **kwargs):

    if not created:
        return

    create_notification(
        recipient=instance.post.author,
        sender=instance.user,
        notification_type=Notification.NotificationType.LIKE,
        message=f"{instance.user.username} liked your post.",
    )

@receiver(post_save, sender=Follow)
def follow_notification(sender, instance, created, **kwargs):

    if not created:
        return

    create_notification(
        recipient=instance.following,
        sender=instance.follower,
        notification_type=Notification.NotificationType.FOLLOW,
        message=f"{instance.follower.username} started following you.",
    )