from django.urls import path

from .views import (
    FollowUserView,
    FollowersListView,
    FollowingListView,
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
    path(
        "<str:username>/followers/",
        FollowersListView.as_view(),
        name="followers-list",
    ),
    path(
    "<str:username>/following/",
    FollowingListView.as_view(),
    name="following-list",
),
]