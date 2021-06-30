from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer, ClienteSerializer
from rest_framework import viewsets, status, generics
from django.contrib.auth.models import User
from .models import Cliente
from rest_framework.views import APIView
from rest_framework import permissions
# Create your views here.


from django.contrib.auth import authenticate


class TokenList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = self.request.user
        return Response({"token": user.auth_token.key})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
