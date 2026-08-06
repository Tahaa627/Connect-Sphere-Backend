from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CommentSerializer
from .services import create_comment


class CreateCommentView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        try:

            comment = create_comment(
                author=request.user,
                post_id=request.data.get("post"),
                parent_id=request.data.get("parent"),
                content=request.data.get("content"),
            )

        except ValueError as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = CommentSerializer(comment)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

from rest_framework.generics import ListAPIView

from .selectors import get_post_comments
from .serializers import CommentSerializer
from apps.core.pagination import DefaultPagination

class PostCommentsView(ListAPIView):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = CommentSerializer

    pagination_class = DefaultPagination

    def get_queryset(self):

        post_id = self.kwargs["post_id"]

        return get_post_comments(post_id)