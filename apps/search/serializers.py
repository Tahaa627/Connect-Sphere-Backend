from django.contrib.auth import get_user_model
from rest_framework import serializers
from apps.posts.models import Hashtag,Post

User = get_user_model()


class UserSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )



class PostSearchSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()

    class Meta:

        model = Post

        fields = (
            "id",
            "author",
            "content",
            "created_at",
        )

    def get_author(self, obj):

        return {
            "id": obj.author.id,
            "username": obj.author.username,
        }


class HashtagSearchSerializer(serializers.ModelSerializer):

    posts_count = serializers.IntegerField(
        read_only=True
    )

    class Meta:

        model = Hashtag

        fields = (
            "id",
            "name",
            "posts_count",
        )


class UserSuggestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            "id",
            "username",
        )

class HashtagSuggestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Hashtag

        fields = (
            "id",
            "name",
        )

class PostSuggestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post

        fields = (
            "id",
            "content",
        )

class PostSuggestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post

        fields = (
            "id",
            "content",
        )