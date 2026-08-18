
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/",include("apps.accounts.urls"),),
    path("api/profiles/", include("apps.profiles.urls")),
    path("api/posts/",include("apps.posts.urls"),),
    path("api/comments/",include("apps.comments.urls")),
    path("api/likes/",include("apps.likes.urls")),
    path("api/followers/",include("apps.followers.urls")),
    path("api/notifications/",include("apps.notifications.urls")),
    path("api/messages/",include("apps.messaging.urls")),
    path("api/search/",include("apps.search.urls")),
    path("api/moderation/",include("apps.moderation.urls"),),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )