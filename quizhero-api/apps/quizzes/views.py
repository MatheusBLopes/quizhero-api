from rest_framework import viewsets

from apps.quizzes.models import Answer, Category, Question, Quiz
from apps.quizzes.serializers import AnswerSerializer, CategorySerializer, QuestionSerializer, QuizSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizViewSet(viewsets.ModelViewSet):
    lookup_field = "code"
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
