from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Manager
from clients.models import Client
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import routers, serializers, viewsets, mixins
from rest_framework.decorators import action
from .serializer import ManagerSerializer, ClientSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions
import copy


def get_manager_by_username(request, username):
    try:
        obj = Manager.objects.get(id=username)
        return HttpResponse (obj.title)
    except ObjectDoesNotExist:
        return  HttpResponse ("ObjectDoesNotExist")

class IsManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #raise Exception (obj.manager.id, request.user.id)
        return obj.manager_id == request.user.id

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [IsManager]
    serializer_class = ClientSerializer

    def get_queryset(self):
        if Manager.is_admin == True:
            return [permissions.AllowAny()]
            
        # return self.queryset
        queryset = self.queryset.filter(manager_id = self.request.user.id)
        page = self.request.query_params.get('page', 0)
        offset = 5
        if page:
            return queryset[int(page)*offset:int(page)*offset + offset]
        return queryset

    def create(self, request, *args, **kwargs):
        if Manager.is_admin == True:
            return [permissions.AllowAny()]
        # data = copy.deepcopy(request.data) 
        # data["manager_id"] = request.user.id
        client = self.get_serializer(data=request.data)
        client.is_valid(raise_exception=True)
        self.perform_create(client)
        headers = self.get_success_headers(client.data)
        Client.objects.filter(id = client.data["id"]).update(manager_id = request.user.id)
        return Response(request.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        if Manager.is_admin == True:
            return [permissions.AllowAny()]

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        # client = Client.objects.filter(id = instance.id)
        # client.update(id= instance.id, **request.data)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        if Manager.is_admin == True:
            return [permissions.AllowAny()]
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)




class ManagerPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    permission_classes = [ManagerPermissions]
    serializer_class = ManagerSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Manager.objects.all()
        return Manager.objects.filter(id = self.request.user.id)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        user = Manager(email=request.data['email'], id = instance.id)
        user.set_password(request.data['password'])
        user.save()
        return Response(user.email)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# def get_users_list(request):
#   if request.method == "GET":
#       queryset = Client.objects.all()
#       serializer =ClientSerializer(queryset, many = True)
#       return JsonResponse (serializer.data)
