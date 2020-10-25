from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Manager
from users.models import Client

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ['url', 'client_id', 'is_admin']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['url', 'mobile']
