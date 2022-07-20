from rest_framework import viewsets

from apps.quizzes.models import Category, Quiz
from apps.quizzes.serializers import CategorySerializer, QuizSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
