from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Manager
from clients.models import Client
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import routers, serializers, viewsets, mixins
from rest_framework.decorators import action
from .serializer import ManagerSerializer, ClientSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


def get_manager_by_username(request, username):
    try:
        obj = Manager.objects.get(id=username)
        return HttpResponse (obj.title)
    except ObjectDoesNotExist:
        return  HttpResponse ("ObjectDoesNotExist")


class UserViewSet(viewsets.ModelViewSet):
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

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ManagerSerializer

    def get_queryset(self):
        if self.request.user.is_admin:
            return Manager.objects.all()
        return Manager.objects.filter(id = self.request.user.id)

    # def create(self, request, *args, **kwargs):      
    #     user = Manager(email=request.data['email'])
    #     user.set_password(request.data['password'])
    #     user.save()
    #     return Response(user.email, status=status.HTTP_201_CREATED)

    # # def update(self, request, *args, **kwargs):
    # #     return self.partial_update(request, *args, **kwargs)
 
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        user = Manager(instance, email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        return Response(user.email)

    # def destroy(self, request, *args, **kwargs):
    #     user = Manager(email=request.data['email'])
    #     user.set_password(request.data['password'])
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class LoginLogout(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response()


# def get_users_list(request):
#   if request.method == "GET":
#       queryset = Client.objects.all()
#       serializer =ClientSerializer(queryset, many = True)
#       return JsonResponse (serializer.data)
