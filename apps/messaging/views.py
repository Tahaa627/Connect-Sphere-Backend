from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import get_user
from .serializers import StartConversationSerializer
from .services import get_or_create_conversation

from rest_framework.generics import ListAPIView
from apps.core.pagination import DefaultPagination
from .selectors import get_user_conversations
from .serializers import ConversationSerializer

from .selectors import get_conversation
from .services import send_message
from .serializers import SendMessageSerializer
from .permissions import IsConversationParticipant
from .models import Message

from rest_framework.generics import ListAPIView

from apps.core.pagination import DefaultPagination

from .selectors import (
    get_conversation,
    get_conversation_messages,
)

class StartConversationView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = StartConversationSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        participant = get_user(
            serializer.validated_data["participant_id"]
        )

        conversation = get_or_create_conversation(
            request.user,
            participant,
        )

        return Response(
            {
                "conversation_id": conversation.id
            },
            status=status.HTTP_201_CREATED,
        )

class ConversationListView(ListAPIView):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = ConversationSerializer

    pagination_class = DefaultPagination

    def get_queryset(self):

        return get_user_conversations(
            self.request.user
        )

class SendMessageView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):

        serializer = SendMessageSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        conversation = get_conversation(
            serializer.validated_data["conversation"].id
        )

        permission = IsConversationParticipant()

        if not permission.has_object_permission(
            request,
            self,
            conversation,
        ):
            return Response(
                {
                    "detail": "You are not a participant of this conversation."
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        message = send_message(
            sender=request.user,
            conversation=conversation,
            content=serializer.validated_data["content"],
        )

        return Response(
            {
                "id": message.id,
                "conversation": conversation.id,
                "sender": request.user.username,
                "content": message.content,
                "created_at": message.created_at,
            },
            status=status.HTTP_201_CREATED,
        )

class MessageHistoryView(ListAPIView):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = MessageSerializer

    pagination_class = DefaultPagination

    def get_queryset(self):

        conversation = get_conversation(
            self.kwargs["conversation_id"]
        )

        permission = IsConversationParticipant()

        if not permission.has_object_permission(
            self.request,
            self,
            conversation,
        ):
            return Message.objects.none()

        return get_conversation_messages(
            conversation
        )