from django.urls import path

from .views import MyProfileView, UpdateProfileView, UploadAvatarView, UploadCoverView

urlpatterns = [
    path("me/", MyProfileView.as_view()),
    path("me/update/", UpdateProfileView.as_view()),
    path("me/avatar/",UploadAvatarView.as_view(),),
    path("me/cover/",UploadCoverView.as_view(),),
]