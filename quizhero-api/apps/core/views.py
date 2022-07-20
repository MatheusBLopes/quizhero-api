from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import UUIDUser as User
from apps.core.serializers import ChangePasswordSerializer, RegisterSerializer, UpdateUserSerializer


class PingView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        return Response("Pong", status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        user = User.objects.filter(pk=request.auth["user_id"]).first()
        serializer = ChangePasswordSerializer(user, data=request.data)
        serializer.validate(request.data)

        if serializer.is_valid():
            serializer.update(user, request.data)
            return Response(status=status.HTTP_200_OK)

        return Response(data=serializer.errors["old_password"], status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        user = User.objects.filter(pk=request.auth["user_id"]).first()
        serializer = UpdateUserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.update(user, request.data)
            return Response(status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
