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


def get_manager_by_username(request, username):
    try:
        obj = Manager.objects.get(id=username)
        return HttpResponse (obj.title)
    except ObjectDoesNotExist:
        return  HttpResponse ("ObjectDoesNotExist")


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer

    def listing(request):
        user_list = Client.objects.all()
        paginator = Paginator(user_list, 2)

    def get_queryset(self):
        page = self.request.query_params.get('page', None)
        offset = 2
        if page:
            return self.queryset[int(page)*offset:int(page)*offset + offset]
        return self.queryset
    # @action(detail = False)
    # def last(self, request):
    #   return self.queryset.objects.last()
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


class LoginLogout(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response()


# def get_users_list(request):
#   if request.method == "GET":
#       queryset = Client.objects.all()
#       serializer =ClientSerializer(queryset, many = True)
#       return JsonResponse (serializer.data)
