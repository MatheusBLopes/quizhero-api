from django.urls import include, path
from rest_framework import routers

from apps.quizzes.views import CategoryViewSet, PublicQuizViewSet, QuestionViewSet, QuizViewSet

app_name = "quizzes"

router = routers.DefaultRouter()
router.register("category", CategoryViewSet, basename="Categories")
router.register("quiz", QuizViewSet, basename="Quizzes")
router.register("questions", QuestionViewSet, basename="Questions")

urlpatterns = [
    path("", include(router.urls)),
    path("public/", PublicQuizViewSet.as_view(), name="public_quizzes"),
]
