from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Conversation, Message

User = get_user_model()

class StartConversationSerializer(serializers.Serializer):

    participant_id = serializers.IntegerField()




class ConversationSerializer(serializers.ModelSerializer):

    participant = serializers.SerializerMethodField()

    last_message = serializers.SerializerMethodField()

    last_message_time = serializers.SerializerMethodField()

    class Meta:

        model = Conversation
        unread_count = serializers.IntegerField(read_only=True)
        fields = (
            "id",
            "participant",
            "last_message",
            "last_message_time",
        )
        
    def get_participant(self, obj):

        request = self.context["request"]

        other = obj.participants.exclude(
            id=request.user.id
        ).first()

        if other is None:
            return None

        return {
            "id": other.id,
            "username": other.username,
        }

    def get_last_message(self, obj):

        message = obj.messages.order_by(
            "-created_at"
        ).first()

        return message.content if message else ""

    def get_last_message_time(self, obj):

        message = obj.messages.order_by(
            "-created_at"
        ).first()

        return (
            message.created_at
            if message
            else None
        )

class SendMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message

        fields = (
            "conversation",
            "content",
        )

class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    class Meta:

        model = Message

        fields = (
            "id",
            "sender",
            "content",
            "is_read",
            "created_at",
        )
    def get_content(self, obj):
        if obj.is_deleted:
            return "This message was deleted."
        return obj.content
    
    def get_sender(self, obj):

        return {
            "id": obj.sender.id,
            "username": obj.sender.username,
        }

class MessageSearchSerializer(serializers.ModelSerializer):

    sender = serializers.CharField(
        source="sender.username",
        read_only=True,
    )

    class Meta:

        model = Message

        fields = (
            "id",
            "conversation",
            "sender",
            "content",
            "created_at",
        )