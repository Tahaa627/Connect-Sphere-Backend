from django.conf import settings
from django.db import models


class Notification(models.Model):

    class NotificationType(models.TextChoices):
        FOLLOW = "FOLLOW", "Follow"
        LIKE = "LIKE", "Like"
        COMMENT = "COMMENT", "Comment"
        MENTION = "MENTION", "Mention"

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_notifications",
    )

    notification_type = models.CharField(
        max_length=20,
        choices=NotificationType.choices,
    )

    message = models.CharField(
        max_length=255,
    )

    is_read = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender.username} → {self.recipient.username}"