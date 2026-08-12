from rest_framework import serializers


class StartConversationSerializer(serializers.Serializer):

    participant_id = serializers.IntegerField()