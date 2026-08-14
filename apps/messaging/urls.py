from django.urls import path
from .views import (
    MarkConversationReadView,
    MessageHistoryView,
    StartConversationView,
    ConversationListView,
    SendMessageView,
    UnreadMessageCountView,
)

urlpatterns = [

    path(
        "conversations/",
        StartConversationView.as_view(),
        name="start-conversation",
    ),

    path(
        "conversations/list/",
        ConversationListView.as_view(),
        name="conversation-list",
    ),

    path(
        "conversations/<int:conversation_id>/read/",
        MarkConversationReadView.as_view(),
        name="mark-conversation-read",
    ),

    path(
        "",
        SendMessageView.as_view(),
        name="send-message",
    ),
    path(
        "conversations/<int:conversation_id>/",
        MessageHistoryView.as_view(),
        name="message-history",
    ),
    path(
        "unread-count/",
        UnreadMessageCountView.as_view(),
        name="unread-message-count",
    ),
]