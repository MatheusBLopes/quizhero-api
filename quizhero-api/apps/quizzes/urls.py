from django.urls import path

from apps.quizzes.views import TestQuizView

app_name = "quizzes"

urlpatterns = [path("quizzes/test", TestQuizView.as_view(), name="test-quiz-view")]
