from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class TestQuizView(APIView):
    def get(self, request):
        return Response(True, status=status.HTTP_200_OK)
