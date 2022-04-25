from ast import Is
from users.models import User

from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from .permissions import IsUserOwner

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['usesname'] = user.username
        token['avatar'] = user.avatar
        return token

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class OwnerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'avatar', 'bio', 'date_joined', 'is_staff', 'is_active', 'is_superuser')


class OwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsUserOwner, ]

