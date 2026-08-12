from django.db import transaction

from .models import Conversation, ConversationParticipant


@transaction.atomic
def get_or_create_conversation(user1, user2):
    """
    Return an existing one-to-one conversation
    or create a new one.
    """

    if user1 == user2:
        raise ValueError(
            "You cannot start a conversation with yourself."
        )

    conversations = (
        Conversation.objects.filter(
            participants=user1
        ).filter(
            participants=user2
        )
    )

    for conversation in conversations:
        if conversation.participants.count() == 2:
            return conversation

    conversation = Conversation.objects.create()

    ConversationParticipant.objects.bulk_create([
        ConversationParticipant(
            conversation=conversation,
            user=user1,
        ),
        ConversationParticipant(
            conversation=conversation,
            user=user2,
        ),
    ])

    return conversation