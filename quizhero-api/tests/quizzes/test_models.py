import pytest

from apps.quizzes.models import Quiz

pytestmark = pytest.mark.django_db


class TestQuiz:
    def test_quiz(self, quiz_title):
        quiz = Quiz.objects.create(title=quiz_title)

        assert quiz.title == quiz_title
