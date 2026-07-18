from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Follow

User = get_user_model()


class FollowUserSerializer(serializers.ModelSerializer):
    """
    Serializer used to return information
    about the user being followed.
    """

    username = serializers.CharField(
        source="following.username",
        read_only=True,
    )

    class Meta:
        model = Follow
        fields = (
            "id",
            "username",
            "created_at",
        )