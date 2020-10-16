from django.urls import path, include
from rest_framework import routers, serializers, viewsets
# from books.models import Manager
from users.models import CustomUser

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ['url', 'email', 'client_id', 'is_able', 'is_admin']

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'mobile']
