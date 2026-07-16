from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.serializers import UserSerializer


class MyProfileView(APIView):
    """
    Returns the currently logged-in user's profile.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response(serializer.data)
    
from rest_framework import status
from .serializers import ProfileSerializer

class UpdateProfileView(APIView):
    """
    Update the logged-in user's profile.
    """

    permission_classes = [IsAuthenticated]

    def patch(self, request):
        profile = request.user.profile

        serializer = ProfileSerializer(
            profile,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Profile updated successfully.",
                "profile": serializer.data,
            },
            status=status.HTTP_200_OK,
        )