from django.urls import path

from .views import PostLikesView, ToggleLikeView

urlpatterns = [

    path(
        "toggle/",
        ToggleLikeView.as_view(),
        name="toggle-like",
    ),
    path(
        "post/<int:post_id>/",
        PostLikesView.as_view(),
        name="post-likes",
    ),

]