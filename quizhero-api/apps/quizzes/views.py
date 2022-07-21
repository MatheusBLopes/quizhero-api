from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.quizzes.models import Answer, Category, Favorite, Question, Quiz
from apps.quizzes.permissions import IsAdmindOrReadOnly
from apps.quizzes.serializers import (
    AnswerSerializer,
    CategorySerializer,
    FavoriteSerializer,
    QuestionSerializer,
    QuizSerializer,
)


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


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        user = self.request.user

        return Favorite.objects.filter(user=user)

    def delete(self, request):
        favorite = get_object_or_404(Favorite, quiz=request.data["quiz"])
        favorite.delete()

        return Response(status=204)

    def list(self, request, *args, **kwargs):
        favorites_queryset = self.filter_queryset(self.get_queryset())
        codes_list = [x.quiz.code for x in favorites_queryset]

        quizzes_queryset = Quiz.objects.filter(code__in=codes_list)

        page = self.paginate_queryset(quizzes_queryset)
        if page is not None:
            serializer = QuizSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = QuizSerializer(quizzes_queryset, many=True)
        return Response(serializer.data)
