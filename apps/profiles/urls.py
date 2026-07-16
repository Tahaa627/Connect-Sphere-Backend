from django.urls import path

from .views import MyProfileView, UpdateProfileView

urlpatterns = [
    path("me/", MyProfileView.as_view()),
    path("me/update/", UpdateProfileView.as_view()),
]