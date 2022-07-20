from django.conf.urls import include
from django.urls import path

from apps.core.views import PingView

urlpatterns = [
    path("api/v1/", include("apps.quizzes.urls")),
    path("api/v1/", include("apps.core.urls")),
    path(r"ping/", PingView.as_view(), name="ping"),
]
