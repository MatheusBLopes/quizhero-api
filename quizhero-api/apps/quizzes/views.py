from rest_framework import viewsets

from apps.quizzes.models import Category
from apps.quizzes.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
