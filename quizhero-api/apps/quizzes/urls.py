from django.urls import include, path
from rest_framework import routers

from apps.quizzes.views import CategoryViewSet, QuizViewSet

app_name = "quizzes"

router = routers.DefaultRouter()
router.register("category", CategoryViewSet, basename="Categories")
router.register("quiz", QuizViewSet, basename="Quizzes")

urlpatterns = [path("", include(router.urls))]
