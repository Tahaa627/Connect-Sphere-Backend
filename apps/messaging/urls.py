from django.urls import path
from .views import (
    MessageHistoryView,
    StartConversationView,
    ConversationListView,
    SendMessageView,
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
        "",
        SendMessageView.as_view(),
        name="send-message",
    ),
    path(
        "conversations/<int:conversation_id>/",
        MessageHistoryView.as_view(),
        name="message-history",
    ),
]