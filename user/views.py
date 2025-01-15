from django.shortcuts import render
from rest_framework import generics

from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]

    def get_object(self):
        return self.request.user