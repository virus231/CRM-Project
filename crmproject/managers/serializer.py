from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Manager
from clients.models import Client

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ['url', 'id', 'email', 'first_name', 'last_name', 'password', 'is_admin']
class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['url', 'id', 'first_name', 'last_name', 'mobile', 'status', 'manager']
