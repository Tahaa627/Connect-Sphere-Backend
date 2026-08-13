from django.urls import path
from .views import (
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
]