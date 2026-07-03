from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer
from .services import create_user


class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = create_user(serializer.validated_data)

        return Response(
            {
                "message": "User registered successfully.",
                "username": user.username,
            },
            status=status.HTTP_201_CREATED,
        )
# Create your views here.
