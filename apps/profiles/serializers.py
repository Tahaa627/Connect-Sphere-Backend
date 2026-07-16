from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """

    class Meta:
        model = Profile
        fields = (
            "bio",
            "website",
            "location",
            "birth_date",
            "avatar",
            "cover_photo",
            "is_private",
        )