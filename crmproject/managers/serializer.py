from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Manager
from clients.models import Client

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
<<<<<<< HEAD
        fields = ['url', 'id', 'email', 'is_admin']
=======
        fields = ['url', 'email', 'password', 'is_admin']
>>>>>>> 51381ad5087ada870280c2ab4ba818962110fb5f

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['url', 'first_name', 'last_name', 'mobile', 'status', 'manager']
