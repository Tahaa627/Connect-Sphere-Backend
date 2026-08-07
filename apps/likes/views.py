from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ToggleLikeSerializer
from .services import toggle_like


class ToggleLikeView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = ToggleLikeSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        liked, count = toggle_like(
            request.user,
            serializer.validated_data["post"]
        )

        return Response(
            {
                "liked": liked,
                "like_count": count,
            },
            status=status.HTTP_200_OK,
        )