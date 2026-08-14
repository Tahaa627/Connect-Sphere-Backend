from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from django.db.models import Count, Max
from .models import Conversation

User = get_user_model()


def get_user(user_id):
    """
    Return a user by ID.
    """

    return get_object_or_404(
        User,
        id=user_id,
    )



def get_user_conversations(user):
    """
    Return all conversations for a user ordered
    by most recent activity.
    """

    return (
        Conversation.objects
        .filter(participants=user)
        .prefetch_related(
            "participants",
            "messages",
        )
        .annotate(
            last_activity=Max("messages__created_at"),
        )
        .order_by("-last_activity")
    )

from django.shortcuts import get_object_or_404

from .models import Conversation


def get_conversation(conversation_id):
    """
    Return a conversation by its ID.
    """

    return get_object_or_404(
        Conversation,
        id=conversation_id,
    )

from .models import Message


def get_conversation_messages(conversation):
    """
    Return all messages for a conversation.
    """

    return (
        Message.objects
        .filter(conversation=conversation)
        .select_related("sender")
        .order_by("created_at")
    )