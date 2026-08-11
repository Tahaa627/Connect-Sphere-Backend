# Create your models here.
from django.conf import settings
from django.db import models


class Conversation(models.Model):
    """
    Represents a chat between two or more users.
    """

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="ConversationParticipant",
        related_name="conversations",
    )

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"Conversation {self.id}"