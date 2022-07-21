from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.quizzes.models import Answer, Category, Question, Quiz
from apps.quizzes.permissions import IsAdmindOrReadOnly
from apps.quizzes.serializers import AnswerSerializer, CategorySerializer, QuestionSerializer, QuizSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdmindOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizViewSet(viewsets.ModelViewSet):
    lookup_field = "code"
    serializer_class = QuizSerializer

    def get_queryset(self):
        user = self.request.user

        return Quiz.objects.filter(user=user)


class PublicQuizViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = "code"
    queryset = Quiz.objects.filter(status="Public")
    serializer_class = QuizSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
