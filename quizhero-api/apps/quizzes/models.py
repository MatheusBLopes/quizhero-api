import uuid

from django.db import models

from apps.core.models import UUIDUser as User
from apps.quizzes.utils import generate_quiz_code

STATUS_CHOICES = (
    ("Public", "Public"),
    ("Private", "Private"),
)


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Category(UUIDModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quiz(UUIDModel):
    title = models.CharField(max_length=255, blank=False)
    category = models.ForeignKey(Category, related_name="quizzes", null=True, on_delete=models.SET_NULL)
    code = models.CharField(editable=False, max_length=16, unique=True, default=generate_quiz_code)
    # TODO How to deal with quizzes without users?
    user = models.ForeignKey(User, related_name="quizzes", on_delete=models.CASCADE)
    status = models.CharField(
        max_length=64,
        default="private",
        choices=STATUS_CHOICES,
    )

    def __str__(self):
        return self.title


class Question(UUIDModel):
    description = models.CharField(max_length=10000, blank=False)
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.description


class Answer(UUIDModel):
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=False)
    right_answer = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.description


class Favorite(UUIDModel):
    user = models.ForeignKey(User, related_name="favorites", on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name="favorites", on_delete=models.CASCADE, to_field="code")
