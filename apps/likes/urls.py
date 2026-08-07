from django.urls import path

from .views import ToggleLikeView

urlpatterns = [

    path(
        "toggle/",
        ToggleLikeView.as_view(),
        name="toggle-like",
    ),

]