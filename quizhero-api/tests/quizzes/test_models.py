import pytest

from .factories import UserFactory
from apps.quizzes.models import Quiz

pytestmark = pytest.mark.django_db


class TestQuiz:
    def test_create_quiz(self, quiz_title):
        user = UserFactory()
        quiz = Quiz.objects.create(title=quiz_title, user=user)

        assert quiz.title == quiz_title
