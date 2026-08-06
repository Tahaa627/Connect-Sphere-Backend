from django.urls import path

from .views import (
    CreateCommentView,
    PostCommentsView,
)

urlpatterns = [

    path(
        "",
        CreateCommentView.as_view(),
        name="create-comment",
    ),

    path(
        "post/<int:post_id>/",
        PostCommentsView.as_view(),
        name="post-comments",
    ),
]