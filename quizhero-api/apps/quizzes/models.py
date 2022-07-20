from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField(max_length=255, blank=False)
    category = models.ForeignKey(Category, related_name="quizzes", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Question(models.Model):
    description = models.CharField(max_length=10000, blank=False)
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.description


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=False)
    right_answer = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.description
