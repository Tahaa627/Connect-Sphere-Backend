from django.urls import path

from .views import (
    FollowUserView,
    UnfollowUserView,
)

urlpatterns = [
    path(
        "follow/<str:username>/",
        FollowUserView.as_view(),
        name="follow-user",
    ),

    path(
        "unfollow/<str:username>/",
        UnfollowUserView.as_view(),
        name="unfollow-user",
    ),
]