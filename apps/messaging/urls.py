from django.urls import path

from .views import StartConversationView

urlpatterns = [

    path(
        "conversations/",
        StartConversationView.as_view(),
        name="start-conversation",
    ),

]