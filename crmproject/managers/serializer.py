from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Manager
from clients.models import Client

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ['url', 'email', 'password', 'is_admin']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['url', 'first_name', 'last_name', 'mobile', 'status', 'manager']
