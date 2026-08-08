from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from apps.core.pagination import DefaultPagination

from .serializers import (
    ToggleLikeSerializer,
    LikeUserSerializer,
)

from .services import toggle_like

from .selectors import get_users_who_liked


User = get_user_model()


class ToggleLikeView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = ToggleLikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        liked, count = toggle_like(
            request.user,
            serializer.validated_data["post"],
        )

        return Response(
            {
                "liked": liked,
                "like_count": count,
            },
            status=status.HTTP_200_OK,
        )


class PostLikesView(ListAPIView):

    permission_classes = [IsAuthenticated]

    serializer_class = LikeUserSerializer

    pagination_class = DefaultPagination

    def get_queryset(self):
        return get_users_who_liked(
            self.kwargs["post_id"]
        )