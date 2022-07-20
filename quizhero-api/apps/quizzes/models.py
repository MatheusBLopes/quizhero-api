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
