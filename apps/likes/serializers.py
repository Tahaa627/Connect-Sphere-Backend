from rest_framework import serializers


class ToggleLikeSerializer(serializers.Serializer):

    post = serializers.IntegerField()