from rest_framework import serializers


class ToggleLikeSerializer(serializers.Serializer):

    post = serializers.IntegerField()

from django.contrib.auth import get_user_model

User = get_user_model()


class LikeUserSerializer(serializers.ModelSerializer):

    profile_image = serializers.SerializerMethodField()

    class Meta:

        model = User

        fields = (
            "id",
            "username",
            "profile_image",
        )

    def get_profile_image(self, obj):

        profile = getattr(obj, "profile", None)

        if profile and profile.profile_image:
            return profile.profile_image.url

        return None 