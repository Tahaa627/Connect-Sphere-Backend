from xml.etree.ElementTree import Comment

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.likes.models import Like
from .models import Notification
from .services import create_notification

from apps.followers.models import Follow

from django.contrib.auth import get_user_model

from .utils import extract_mentions

User = get_user_model()

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

@receiver(post_save, sender=Comment)
def comment_notification(sender, instance, created, **kwargs):

    if not created:
        return

    create_notification(
        recipient=instance.post.author,
        sender=instance.author,
        notification_type=Notification.NotificationType.COMMENT,
        message=f"{instance.author.username} commented on your post.",
    )

@receiver(post_save, sender=Comment)
def mention_notification(sender, instance, created, **kwargs):

    if not created:
        return

    usernames = extract_mentions(
        instance.content
    )

    for username in usernames:

        try:

            user = User.objects.get(
            username=username
            )

            if user == instance.author:
                continue

            create_notification(
                recipient=user,
                sender=instance.author,
                notification_type=Notification.NotificationType.MENTION,
                message=f"{instance.author.username} mentioned you in a comment.",
        )

        except User.DoesNotExist:
            continue