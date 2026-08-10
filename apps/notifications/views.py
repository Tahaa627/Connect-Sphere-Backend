from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.core.pagination import DefaultPagination

from .selectors import get_user_notifications
from .serializers import NotificationSerializer


class NotificationListView(ListAPIView):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = NotificationSerializer

    pagination_class = DefaultPagination

    def get_queryset(self):
        return get_user_notifications(
            self.request.user
        )