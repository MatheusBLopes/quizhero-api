import uuid

from django.db import models

from apps.quizzes.utils import generate_quiz_code


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
