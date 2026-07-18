from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FollowUserSerializer
from .services import follow_user


class FollowUserView(APIView):
    """
    Follow another user.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, username):

        result = follow_user(
            follower=request.user,
            username=username,
        )

        if not result["success"]:
            return Response(
                {
                    "message": result["message"]
                },
                status=result["status"],
            )

        serializer = FollowUserSerializer(result["follow"])

        return Response(
            {
                "message": "User followed successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )