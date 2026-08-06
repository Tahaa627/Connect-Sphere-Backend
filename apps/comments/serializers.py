from rest_framework import serializers
from .models import Comment

class RecursiveCommentSerializer(serializers.ModelSerializer):

    author = serializers.CharField(
        source="author.username",
        read_only=True,
    )

    replies = serializers.SerializerMethodField()

    class Meta:

        model = Comment

        fields = (
            "id",
            "author",
            "content",
            "created_at",
            "replies",
        )

    def get_replies(self, obj):

        serializer = RecursiveCommentSerializer(
            obj.replies.all(),
            many=True,
        )

        return serializer.data


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.CharField(
        source="author.username",
        read_only=True,
    )

    replies = RecursiveCommentSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = Comment

        fields = (
            "id",
            "author",
            "content",
            "created_at",
            "replies",
        )