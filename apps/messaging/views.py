from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import get_user
from .serializers import StartConversationSerializer
from .services import get_or_create_conversation


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